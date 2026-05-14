#!/usr/bin/env python3
import argparse, datetime, hashlib, html, json, os, re, sys, time, urllib.parse, urllib.request
from pathlib import Path
from bs4 import BeautifulSoup

TODAY = datetime.date.today().isoformat()
UA = 'Mozilla/5.0 raw-source-upgrade/1.0'

def sha(s): return hashlib.sha256(s.encode('utf-8', errors='replace')).hexdigest()

def fetch_text(url, timeout=60):
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': 'text/html,application/json,text/plain,*/*'})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = r.read()
        ctype = r.headers.get('content-type','')
    enc='utf-8'
    m=re.search(r'charset=([^;]+)', ctype)
    if m: enc=m.group(1)
    return data.decode(enc, errors='replace')

def clean_ws(s):
    s = re.sub(r'\n\s*\n\s*\n+', '\n\n', s)
    return s.strip()

def html_to_md(url):
    raw = fetch_text(url)
    try:
        from readability import Document
        doc = Document(raw)
        title = doc.short_title()
        content_html = doc.summary(html_partial=True)
    except Exception:
        soup = BeautifulSoup(raw, 'lxml')
        title = soup.title.get_text(' ', strip=True) if soup.title else url
        for tag in soup(['script','style','noscript','svg','form','nav','footer','header']): tag.decompose()
        content_html = str(soup.body or soup)
    import html2text
    h = html2text.HTML2Text()
    h.ignore_images = False
    h.ignore_links = False
    h.body_width = 0
    md = h.handle(content_html)
    return title, clean_ws(md), len(raw)

def hn_thread(item_id):
    def get_json(url): return json.loads(fetch_text(url, timeout=60))
    root = get_json(f'https://hacker-news.firebaseio.com/v0/item/{item_id}.json')
    lines=[]
    lines.append(f'# {root.get("title", "HN item "+str(item_id))}')
    lines.append('')
    lines.append(f'- HN item id: {item_id}')
    lines.append(f'- URL: https://news.ycombinator.com/item?id={item_id}')
    if root.get('url'): lines.append(f'- Linked URL: {root.get("url")}')
    lines.append(f'- By: {root.get("by")}')
    lines.append(f'- Score: {root.get("score")}')
    lines.append(f'- Descendants/comments: {root.get("descendants")}')
    lines.append(f'- Time: {root.get("time")}')
    if root.get('text'):
        lines += ['', '## Submission Text', html.unescape(re.sub('<[^<]+?>','',root.get('text','')))]
    lines += ['', '## Comments']
    count=0
    def walk(ids, depth=0):
        nonlocal count
        for cid in ids or []:
            try:
                c=get_json(f'https://hacker-news.firebaseio.com/v0/item/{cid}.json')
            except Exception as e:
                lines.append(f'\n[failed to fetch comment {cid}: {e}]')
                continue
            if c.get('deleted') or c.get('dead'): continue
            count+=1
            indent='  '*depth
            text=c.get('text','')
            text=BeautifulSoup(html.unescape(text), 'lxml').get_text('\n', strip=True)
            lines.append(f'\n### Comment {cid} by {c.get("by")} depth={depth} time={c.get("time")}')
            lines.append('')
            lines.append(text)
            walk(c.get('kids'), depth+1)
    walk(root.get('kids'),0)
    lines.insert(8, f'- Comments fetched: {count}')
    return root.get('title','HN thread'), '\n'.join(lines), count

def write_raw(path, *, source_url, fetched_url, source_type, author, source_date, reliability, body_title, parsed_text, raw_preservation, extraction_method, extra_meta=None):
    extra_meta = extra_meta or {}
    body=f"""# {body_title}

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
    fm={'source_url':source_url,'fetched_url':fetched_url,'source_type':source_type,'author':author,'source_date':source_date,'ingested':TODAY,'sha256':sha(body),'raw_preservation':raw_preservation,'extraction_method':extraction_method}
    fm.update(extra_meta)
    front='---\n'+''.join(f'{k}: {v}\n' for k,v in fm.items())+'---\n\n'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(front+body, encoding='utf-8')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--wiki', default='/Users/a17/wiki'); args=ap.parse_args(); wiki=Path(args.wiki)
    web_sources=[
        ('raw/articles/anthropic-effective-agents-2024.md','https://www.anthropic.com/research/building-effective-agents','blog','Anthropic','2024-12-19','high'),
        ('raw/articles/anthropic-multi-agent-research-2025.md','https://www.anthropic.com/engineering/built-multi-agent-research-system','blog','Anthropic','2025-06-13','high'),
        ('raw/articles/langchain-context-engineering-2025.md','https://www.langchain.com/blog/context-engineering-for-agents','blog','LangChain Team','2025-07-02','medium-high'),
        ('raw/articles/harrison-chase-sequoia-context-engineering-2025.md','https://sequoiacap.com/podcast/context-engineering-our-way-to-long-horizon-agents-langchains-harrison-chase/','interview','Harrison Chase / Sequoia','2025','medium-high'),
        ('raw/articles/simon-willison-embeddings-2023.md','https://simonwillison.net/2023/Oct/23/embeddings/','blog','Simon Willison','2023-10-23','high'),
        ('raw/articles/microsoft-vector-search-not-enough-2024.md','https://techcommunity.microsoft.com/blog/azuredevcommunityblog/doing-rag-vector-search-is-not-enough/4161073','blog','Pamela Fox / Microsoft','2024-06-06','high'),
        ('raw/product-docs/openai-chatgpt-memory-2024-2025.md','https://openai.com/index/memory-and-new-controls-for-chatgpt/','product-docs','OpenAI','2024-02-13; updated 2025','high'),
        ('raw/product-docs/letta-memory-2026.md','https://docs.letta.com/letta-code/memory','product-docs','Letta','captured 2026-05-14','high'),
    ]
    results=[]
    for rel,url,typ,author,sdate,relia in web_sources:
        try:
            title, md, raw_len = html_to_md(url)
            write_raw(wiki/rel, source_url=url, fetched_url=url, source_type=typ, author=author, source_date=sdate, reliability=relia, body_title=title, parsed_text=md, raw_preservation='full_html_article_text_candidate', extraction_method='readability_lxml_html2text', extra_meta={'html_bytes':raw_len, 'parsed_chars':len(md)})
            results.append({'path':rel,'status':'ok','chars':len(md),'html_bytes':raw_len})
        except Exception as e:
            results.append({'path':rel,'status':'error','error':repr(e)})
        time.sleep(1)
    hn=[
        ('raw/community/hn-karpathy-style-wiki-2026.md','47899844','HN: A Karpathy-style LLM wiki your agents maintain','2026'),
        ('raw/community/hn-memgpt-2023.md','37894403','HN: MemGPT: Towards LLMs as Operating Systems','2023-10-15'),
        ('raw/community/hn-letta-code-2025.md','46294274','HN: Letta Code','2025'),
    ]
    for rel,item_id,author,sdate in hn:
        try:
            title, text, count=hn_thread(item_id)
            url=f'https://news.ycombinator.com/item?id={item_id}'
            write_raw(wiki/rel, source_url=url, fetched_url=f'https://hacker-news.firebaseio.com/v0/item/{item_id}.json', source_type='hn', author=author, source_date=sdate, reliability='medium', body_title=title, parsed_text=text, raw_preservation='full_hn_api_thread_text', extraction_method='hacker_news_firebase_api_recursive_comments', extra_meta={'hn_item_id':item_id, 'comments_fetched':count, 'parsed_chars':len(text)})
            results.append({'path':rel,'status':'ok','chars':len(text),'comments':count})
        except Exception as e:
            results.append({'path':rel,'status':'error','error':repr(e)})
        time.sleep(1)
    print(json.dumps(results, indent=2))

if __name__=='__main__': main()
