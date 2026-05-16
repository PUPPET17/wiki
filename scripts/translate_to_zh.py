#!/usr/bin/env python3
"""Translate wiki markdown from English to Simplified Chinese.
Uses multiple providers with automatic fallback:
1. XFYun/NiuTrans-style signed API (if credentials present)
2. Google Translate via deep-translator
Preserves frontmatter, code blocks, blank lines, and basic markdown structure.
"""

import base64
import hashlib
import hmac
import json
import os
import re
import sys
import time
import urllib.request
from email.utils import formatdate
from pathlib import Path

from deep_translator import GoogleTranslator

SRC_DIR = Path('/Users/a17/wiki')
DST_DIR = SRC_DIR / 'zh'
SKIP_DIRS = {'.git', '.vitepress', 'node_modules', 'zh', 'scripts'}
CHUNK_LIMIT = 4500
SEPARATOR = '\n\n⟦SEP⟧\n\n'

XFYUN_APP_ID = os.getenv('XFYUN_APP_ID') or os.getenv('NIUTRANS_APP_ID')
XFYUN_API_KEY = os.getenv('XFYUN_API_KEY') or os.getenv('NIUTRANS_API_KEY')
XFYUN_API_SECRET = os.getenv('XFYUN_API_SECRET') or os.getenv('NIUTRANS_API_SECRET')
XFYUN_URL = 'https://ntrans.xfyun.cn/v2/ots'
XFYUN_HOST = 'ntrans.xfyun.cn'

google_translator = GoogleTranslator(source='en', target='zh-CN')
call_count = 0
provider_counts = {'xfyun': 0, 'google': 0}


def sha256_base64(data: bytes) -> str:
    return base64.b64encode(hashlib.sha256(data).digest()).decode()


def xfyun_translate(text: str) -> str:
    body_obj = {
        'common': {'app_id': XFYUN_APP_ID},
        'business': {'from': 'en', 'to': 'cn'},
        'data': {'text': base64.b64encode(text.encode('utf-8')).decode('ascii')},
    }
    body = json.dumps(body_obj, ensure_ascii=False, separators=(',', ':')).encode('utf-8')
    date = formatdate(timeval=None, localtime=False, usegmt=True)
    digest = 'SHA-256=' + sha256_base64(body)
    request_line = 'POST /v2/ots HTTP/1.1'
    signature_origin = f'host: {XFYUN_HOST}\n' f'date: {date}\n' f'{request_line}\n' f'digest: {digest}'
    signature = base64.b64encode(
        hmac.new(XFYUN_API_SECRET.encode('utf-8'), signature_origin.encode('utf-8'), hashlib.sha256).digest()
    ).decode('ascii')
    authorization = (
        f'api_key="{XFYUN_API_KEY}", algorithm="hmac-sha256", '
        f'headers="host date request-line digest", signature="{signature}"'
    )

    req = urllib.request.Request(
        XFYUN_URL,
        data=body,
        method='POST',
        headers={
            'Content-Type': 'application/json',
            'Accept': 'application/json,version=1.0',
            'Host': XFYUN_HOST,
            'Date': date,
            'Digest': digest,
            'Authorization': authorization,
        },
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        raw = resp.read().decode('utf-8')
    data = json.loads(raw)
    if data.get('code') != 0:
        raise RuntimeError(f"xfyun code={data.get('code')} message={data.get('message')}")
    return data['data']['result']['trans_result']['dst']


def google_translate(text: str) -> str:
    return google_translator.translate(text)


def provider_order():
    providers = []
    if XFYUN_APP_ID and XFYUN_API_KEY and XFYUN_API_SECRET:
        providers.append(('xfyun', xfyun_translate))
    providers.append(('google', google_translate))
    return providers


def api_call(text):
    global call_count
    last_error = None
    for provider_name, provider_fn in provider_order():
        for attempt in range(3):
            try:
                result = provider_fn(text)
                call_count += 1
                provider_counts[provider_name] = provider_counts.get(provider_name, 0) + 1
                if call_count % 30 == 0:
                    time.sleep(2)
                else:
                    time.sleep(0.15)
                return result if result else text
            except Exception as e:
                last_error = e
                wait = min(8, 2 * (attempt + 1))
                print(f'    [{provider_name} retry {attempt+1}] {e}', file=sys.stderr, flush=True)
                time.sleep(wait)
        print(f'    provider fallback: {provider_name} -> next', file=sys.stderr, flush=True)
    print(f'    [all providers failed] keeping source text; last_error={last_error}', file=sys.stderr, flush=True)
    return text


def translate_batch(texts):
    if not texts:
        return []
    if len(texts) == 1:
        t = texts[0]
        if len(t) <= CHUNK_LIMIT:
            return [api_call(t)]
        lines = t.split('\n')
        chunks, cur, cur_len = [], [], 0
        for line in lines:
            if cur_len + len(line) + 1 > CHUNK_LIMIT and cur:
                chunks.append('\n'.join(cur))
                cur, cur_len = [line], len(line)
            else:
                cur.append(line)
                cur_len += len(line) + 1
        if cur:
            chunks.append('\n'.join(cur))
        return ['\n'.join(api_call(c) for c in chunks)]

    combined = SEPARATOR.join(texts)
    if len(combined) <= CHUNK_LIMIT:
        result = api_call(combined)
        parts = re.split(r'\s*⟦SEP⟧\s*', result)
        if len(parts) != len(texts):
            return [api_call(t) if len(t) <= CHUNK_LIMIT else translate_batch([t])[0] for t in texts]
        return parts

    mid = len(texts) // 2
    return translate_batch(texts[:mid]) + translate_batch(texts[mid:])


def parse_file(content):
    lines = content.split('\n')
    segments = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]

        if i == 0 and line.strip() == '---':
            fm = [line]
            i += 1
            while i < n:
                fm.append(lines[i])
                if lines[i].strip() == '---':
                    i += 1
                    break
                i += 1
            segments.append(('raw', '\n'.join(fm)))
            continue

        if re.match(r'^(`{3}|~{3})', line):
            fence_char = line[0]
            fence_len = len(re.match(r'^(`+|~+)', line).group(1))
            code = [line]
            i += 1
            while i < n:
                code.append(lines[i])
                if re.match(r'^' + re.escape(fence_char) + '{' + str(fence_len) + r',}\s*$', lines[i]):
                    i += 1
                    break
                i += 1
            segments.append(('raw', '\n'.join(code)))
            continue

        if not line.strip():
            segments.append(('raw', line))
            i += 1
            continue

        if re.match(r'^\|[-:\s|]+\|$', line.strip()):
            segments.append(('raw', line))
            i += 1
            continue

        if re.match(r'^\s*https?://', line.strip()):
            segments.append(('raw', line))
            i += 1
            continue

        if '![' in line or re.search(r'\[[^\]]+\]\([^\)]+\)', line):
            segments.append(('raw', line))
            i += 1
            continue

        para = []
        while i < n:
            l = lines[i]
            if not l.strip():
                break
            if re.match(r'^(`{3}|~{3})', l):
                break
            para.append(l)
            i += 1
        segments.append(('text', '\n'.join(para)))

    return segments


def translate_file(src_path):
    content = src_path.read_text(errors='replace')
    segments = parse_file(content)
    result_parts = []
    text_batch = []
    text_indices = []

    for idx, (stype, stext) in enumerate(segments):
        result_parts.append(None)
        if stype == 'text':
            text_batch.append(stext)
            text_indices.append(idx)
        else:
            result_parts[idx] = stext

    if text_batch:
        translated = translate_batch(text_batch)
        for i, tidx in enumerate(text_indices):
            result_parts[tidx] = translated[i] if i < len(translated) else text_batch[i]

    return '\n'.join(p for p in result_parts if p is not None)


def main():
    files = []
    for p in sorted(SRC_DIR.rglob('*.md')):
        rel = p.relative_to(SRC_DIR)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        files.append(rel)

    active = ', '.join(name for name, _ in provider_order())
    print(f'Providers: {active}', flush=True)
    print(f'Files to translate: {len(files)}', flush=True)

    for idx, rel in enumerate(files, 1):
        src = SRC_DIR / rel
        dst = DST_DIR / rel
        dst.parent.mkdir(parents=True, exist_ok=True)

        if dst.exists() and dst.stat().st_mtime > src.stat().st_mtime:
            print(f'[{idx}/{len(files)}] SKIP {rel}', flush=True)
            continue

        sz = src.stat().st_size
        print(f'[{idx}/{len(files)}] {rel} ({sz}B)...', end='', flush=True)
        translated = translate_file(src)
        dst.write_text(translated)
        print(f' done ({call_count} calls; xfyun={provider_counts.get("xfyun",0)} google={provider_counts.get("google",0)})', flush=True)

    print(f'\nAll done. total_calls={call_count} xfyun={provider_counts.get("xfyun",0)} google={provider_counts.get("google",0)} output={DST_DIR}/', flush=True)


if __name__ == '__main__':
    main()
