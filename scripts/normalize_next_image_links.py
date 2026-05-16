#!/usr/bin/env python3
from pathlib import Path
from urllib.parse import urlparse, parse_qs, unquote
import re

ROOTS = [Path('/Users/a17/wiki/raw'), Path('/Users/a17/wiki/zh/raw')]
pat = re.compile(r'!\[(.*?)\]\((/_next/image\?[^)]+)\)')

changed_files = 0
changed_refs = 0

for root in ROOTS:
    for path in sorted(root.rglob('*.md')):
        text = path.read_text(errors='replace')
        def repl(m):
            global changed_refs
            alt = m.group(1)
            raw = m.group(2)
            qs = parse_qs(urlparse(raw).query)
            url = qs.get('url', [''])[0]
            if not url:
                return m.group(0)
            changed_refs += 1
            return f'![{alt}]({unquote(url)})'
        new_text = pat.sub(repl, text)
        if new_text != text:
            path.write_text(new_text)
            changed_files += 1
            print(path)

print(f'changed_files={changed_files} changed_refs={changed_refs}')
