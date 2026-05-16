#!/usr/bin/env python3
from pathlib import Path
import re

SRC_ROOT = Path('/Users/a17/wiki/raw')
DST_ROOT = Path('/Users/a17/wiki/zh/raw')

changed_files = 0
changed_lines = 0

link_pat = re.compile(r'!?\[[^\]]*\]\([^\)]*\)')

for src in sorted(SRC_ROOT.rglob('*.md')):
    rel = src.relative_to(SRC_ROOT)
    dst = DST_ROOT / rel
    if not dst.exists():
        continue
    src_lines = src.read_text(errors='replace').splitlines()
    dst_lines = dst.read_text(errors='replace').splitlines()
    limit = min(len(src_lines), len(dst_lines))
    local_changes = 0
    for i in range(limit):
        s = src_lines[i]
        d = dst_lines[i]
        if '![](' in s or link_pat.search(s) or '/_next/image?' in s or '/_next/image?' in d:
            if d != s:
                dst_lines[i] = s
                local_changes += 1
    if local_changes:
        dst.write_text('\n'.join(dst_lines) + ('\n' if dst.read_text(errors='replace').endswith('\n') else ''))
        changed_files += 1
        changed_lines += local_changes
        print(f'{rel}: fixed {local_changes} lines')

print(f'changed_files={changed_files} changed_lines={changed_lines}')
