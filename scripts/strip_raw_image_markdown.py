#!/usr/bin/env python3
from pathlib import Path
import re

ROOTS = [Path('/Users/a17/wiki/zh/raw')]
img_pat = re.compile(r'!\[(.*?)\]\(([^)]+)\)')
changed_files = 0
changed_refs = 0

for root in ROOTS:
    for path in sorted(root.rglob('*.md')):
        text = path.read_text(errors='replace')
        def repl(m):
            global changed_refs
            alt, url = m.group(1), m.group(2)
            changed_refs += 1
            label = alt.strip() or 'image'
            return f'Image: {label} ({url})'
        new_text = img_pat.sub(repl, text)
        if new_text != text:
            path.write_text(new_text)
            changed_files += 1
            print(path)

print(f'changed_files={changed_files} changed_refs={changed_refs}')
