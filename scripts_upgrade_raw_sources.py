#!/usr/bin/env python3
import argparse, datetime, hashlib, html, json, os, re, sys, time, urllib.error, urllib.parse, urllib.request
from pathlib import Path

TODAY = datetime.date.today().isoformat()
UA = 'Mozilla/5.0 raw-source-upgrade/1.0 (+https://example.invalid)'


def sha(s: str) -> str:
    return hashlib.sha256(s.encode('utf-8', errors='replace')).hexdigest()


def fetch(url: str, timeout=60) -> bytes:
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': '*/*'})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def strip_frontmatter(text: str) -> str:
    if text.startswith('---'):
        parts = text.split('---', 2)
        if len(parts) == 3:
            return parts[2].lstrip('\n')
    return text


def read_existing_metadata(path: Path):
    text = path.read_text(encoding='utf-8', errors='replace') if path.exists() else ''
    meta = {}
    if text.startswith('---'):
        parts = text.split('---', 2)
        if len(parts) >= 3:
            for line in parts[1].splitlines():
                if ':' in line:
                    k, v = line.split(':', 1)
                    meta[k.strip()] = v.strip()
    return meta, text


def write_raw(path: Path, *, source_url, fetched_url, source_type, author, source_date, reliability, body_title, parsed_text, raw_preservation, extraction_method, extra_meta=None):
    extra_meta = extra_meta or {}
    body = f"""# {body_title}

## Source Metadata

- Source URL: {source_url}
- Fetched URL: {fetched_url}
- Source type: {source_type}
- Author: {author}
- Source date: {source_date}
- Ingested: {TODAY}
- Reliability: {reliability}
- Raw preservation status: {raw_preservation}
- Extraction method: {extraction_method}

## Parsed Source Text

{parsed_text.strip() if parsed_text.strip() else '[NO PARSED SOURCE TEXT AVAILABLE — extraction failed or source inaccessible]'}
"""
    fm = {
        'source_url': source_url,
        'fetched_url': fetched_url,
        'source_type': source_type,
        'author': author,
        'source_date': source_date,
        'ingested': TODAY,
        'sha256': sha(body),
        'raw_preservation': raw_preservation,
        'extraction_method': extraction_method,
    }
    fm.update(extra_meta)
    front = '---\n' + ''.join(f'{k}: {v}\n' for k, v in fm.items()) + '---\n\n'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(front + body, encoding='utf-8')


def arxiv_pdf_to_text(arxiv_id: str):
    import fitz
    pdf_url = f'https://arxiv.org/pdf/{arxiv_id}'
    data = fetch(pdf_url, timeout=120)
    doc = fitz.open(stream=data, filetype='pdf')
    pages = []
    for i, page in enumerate(doc, start=1):
        txt = page.get_text('text')
        pages.append(f'\n\n<!-- page {i} -->\n\n' + txt)
    return pdf_url, ''.join(pages), len(data), doc.page_count


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--wiki', default='/Users/a17/wiki')
    args = ap.parse_args()
    wiki = Path(args.wiki)
    papers = [
        ('raw/papers/memgpt-2023.md','2310.08560','MemGPT: Towards LLMs as Operating Systems','Charles Packer et al.','2023-10-12'),
        ('raw/papers/generative-agents-2023.md','2304.03442','Generative Agents: Interactive Simulacra of Human Behavior','Joon Sung Park et al.','2023-04-07'),
        ('raw/papers/coala-2023.md','2309.02427','Cognitive Architectures for Language Agents','Theodore R. Sumers et al.','2023-09-05'),
        ('raw/papers/rag-survey-2023.md','2312.10997','Retrieval-Augmented Generation for Large Language Models: A Survey','Yunfan Gao et al.','2023-12-18'),
        ('raw/papers/raptor-2024.md','2401.18059','RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval','Parth Sarthi et al.','2024-01-31'),
        ('raw/papers/self-rag-2023.md','2310.11511','Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection','Akari Asai et al.','2023-10-17'),
        ('raw/papers/memorag-2024.md','2409.05591','MemoRAG: Boosting Long Context Processing with Global Memory-Enhanced Retrieval Augmentation','Hongjin Qian et al.','2024-09-09'),
    ]
    results=[]
    for rel, aid, title, author, sdate in papers:
        path = wiki / rel
        try:
            fetched_url, text, pdf_bytes, pages = arxiv_pdf_to_text(aid)
            source_url = f'https://arxiv.org/abs/{aid}'
            write_raw(path, source_url=source_url, fetched_url=fetched_url, source_type='paper', author=author, source_date=sdate, reliability='high', body_title=title, parsed_text=text, raw_preservation='full_pdf_text', extraction_method='pymupdf_page_text_from_arxiv_pdf', extra_meta={'arxiv_id': aid, 'pdf_bytes': pdf_bytes, 'pdf_pages': pages})
            results.append({'path': rel, 'status':'ok', 'chars':len(text), 'pages':pages})
        except Exception as e:
            results.append({'path': rel, 'status':'error', 'error':repr(e)})
        time.sleep(3.2)
    print(json.dumps(results, indent=2))

if __name__ == '__main__':
    main()
