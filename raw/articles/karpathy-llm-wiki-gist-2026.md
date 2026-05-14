---
source_url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
ingested: 2026-05-14
sha256: ee518b3f4f73dfed92fe95ec033a450bccba58715f370f3dceb4b2498cbad94f
---

# LLM Wiki — Andrej Karpathy Gist

Source URL: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
Author: Andrej Karpathy
Date: 2026-04 (gist/tweet context from X summary indicates Apr 2026)
Type: gist / idea file
Reliability: high for Karpathy's own proposal; speculative for feasibility claims.

Key extracted claims:
- Most RAG systems retrieve raw chunks at query time and re-derive synthesis repeatedly.
- Alternative: LLM incrementally builds and maintains a persistent markdown wiki between the user and raw sources.
- Raw sources are immutable; wiki is LLM-owned; schema instructs agent behavior.
- Operations: ingest, query, lint.
- index.md is content-oriented; log.md is chronological.
- Obsidian can serve as IDE; markdown+git give durability.
- At moderate scale (~100 sources, hundreds of pages), index-first navigation can work before adding embedding infrastructure.
- Good answers should be filed back into the wiki so inquiry compounds.

Direct quote excerpt captured locally via raw gist:
"the wiki is a persistent, compounding artifact. The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you've read."
