#!/usr/bin/env python3
import datetime, hashlib, html, json, re, time, urllib.parse, urllib.request
from pathlib import Path

TODAY = datetime.date.today().isoformat()
WIKI = Path('/Users/a17/wiki')
UA = 'Mozilla/5.0 llm-wiki-research/1.0'

def sha(s):
    return hashlib.sha256(s.encode('utf-8', errors='replace')).hexdigest()

def fetch(url, accept='application/vnd.github+json'):
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': accept})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read().decode('utf-8', errors='replace')

def write_raw(rel, *, source_url, fetched_url, source_type, author, source_date, reliability, title, parsed_text, raw_preservation, extraction_method, extra=None):
    extra = extra or {}
    body = f"""# {title}

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

{parsed_text.strip() if parsed_text.strip() else '[NO PARSED SOURCE TEXT AVAILABLE]'}
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
    fm.update(extra)
    front = '---\n' + ''.join(f'{k}: {v}\n' for k, v in fm.items()) + '---\n\n'
    path = WIKI / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(front + body, encoding='utf-8')
    return {'path': rel, 'chars': len(parsed_text), 'status': raw_preservation}

def gh_issue(owner_repo, num, rel, title_hint, reliability='medium'):
    owner, repo = owner_repo.split('/')
    issue_url = f'https://api.github.com/repos/{owner}/{repo}/issues/{num}'
    comments_url = f'https://api.github.com/repos/{owner}/{repo}/issues/{num}/comments?per_page=100'
    issue = json.loads(fetch(issue_url))
    comments = json.loads(fetch(comments_url))
    lines = []
    lines.append(f"# {issue.get('title')}")
    lines.append('')
    lines.append(f"- GitHub issue: https://github.com/{owner_repo}/issues/{num}")
    lines.append(f"- API URL: {issue_url}")
    lines.append(f"- State: {issue.get('state')}")
    lines.append(f"- Author: {issue.get('user',{}).get('login')}")
    lines.append(f"- Created: {issue.get('created_at')}")
    lines.append(f"- Updated: {issue.get('updated_at')}")
    lines.append(f"- Comments: {issue.get('comments')}")
    labels = ', '.join(l.get('name','') for l in issue.get('labels',[]))
    lines.append(f"- Labels: {labels}")
    lines.append('')
    lines.append('## Issue Body')
    lines.append('')
    lines.append(issue.get('body') or '')
    lines.append('')
    lines.append('## Comments')
    for c in comments:
        lines.append('')
        lines.append(f"### Comment {c.get('id')} by {c.get('user',{}).get('login')} created={c.get('created_at')} updated={c.get('updated_at')}")
        lines.append('')
        lines.append(c.get('body') or '')
    source_url=f'https://github.com/{owner_repo}/issues/{num}'
    source_date=(issue.get('created_at') or 'unknown')[:10]
    return write_raw(rel, source_url=source_url, fetched_url=issue_url, source_type='github issue', author=f"{owner_repo} contributors", source_date=source_date, reliability=reliability, title=title_hint or issue.get('title'), parsed_text='\n'.join(lines), raw_preservation='full_github_issue_api_text', extraction_method='github_rest_issue_and_comments', extra={'github_repo': owner_repo, 'github_issue': num, 'comments_fetched': len(comments)})

def gh_readme(owner_repo, rel, source_type='github repo', reliability='high'):
    owner, repo = owner_repo.split('/')
    api = f'https://api.github.com/repos/{owner}/{repo}'
    meta = json.loads(fetch(api))
    # Try main then master
    candidates = ['main', 'master']
    text = None; raw_url = None
    for branch in candidates:
        url = f'https://raw.githubusercontent.com/{owner}/{repo}/{branch}/README.md'
        try:
            text = fetch(url, accept='text/plain')
            raw_url = url
            break
        except Exception:
            pass
    if text is None:
        text = json.dumps(meta, indent=2)
        raw_url = api
    pre = [f"# Repository metadata: {owner_repo}", '', f"- GitHub URL: https://github.com/{owner_repo}", f"- Description: {meta.get('description')}", f"- Stars: {meta.get('stargazers_count')}", f"- Forks: {meta.get('forks_count')}", f"- Open issues: {meta.get('open_issues_count')}", f"- Created: {meta.get('created_at')}", f"- Updated: {meta.get('updated_at')}", f"- License: {(meta.get('license') or {}).get('spdx_id')}", '', '## README.md', '', text]
    return write_raw(rel, source_url=f'https://github.com/{owner_repo}', fetched_url=raw_url, source_type=source_type, author=f'{owner_repo} maintainers', source_date=(meta.get('created_at') or 'unknown')[:10], reliability=reliability, title=f'GitHub Repository: {owner_repo}', parsed_text='\n'.join(pre), raw_preservation='full_github_readme_text', extraction_method='github_repo_api_and_raw_readme', extra={'github_repo': owner_repo, 'stars': meta.get('stargazers_count'), 'open_issues': meta.get('open_issues_count')})

def gh_raw(url, rel, title, author, source_date='unknown', reliability='medium-high'):
    text = fetch(url, accept='text/plain')
    return write_raw(rel, source_url=url, fetched_url=url, source_type='github raw', author=author, source_date=source_date, reliability=reliability, title=title, parsed_text=text, raw_preservation='full_github_raw_text', extraction_method='raw_githubusercontent', extra={})

results=[]
# GitHub issues/discussions surfaced by search
for args in [
    ('mem0ai/mem0', 4573, 'raw/github/mem0-issue-4573-memory-audit-junk.md', 'mem0 issue 4573: What we found after auditing 10134 mem0 entries: 97.8% were junk', 'medium'),
    ('letta-ai/lettabot', 652, 'raw/github/letta-issue-652-per-conversation-context-scoping.md', 'Letta issue 652: Per-conversation context scoping', 'medium'),
]:
    try:
        results.append(gh_issue(*args))
    except Exception as e:
        results.append({'path': args[2], 'status': 'error', 'error': repr(e)})
    time.sleep(1)

# Repos / READMEs
for owner_repo, rel, reliability in [
    ('mem0ai/mem0', 'raw/github/mem0-repo-readme.md', 'high'),
    ('letta-ai/letta-code', 'raw/github/letta-code-repo-readme.md', 'high'),
    ('nex-crm/wuphf', 'raw/github/wuphf-repo-readme.md', 'medium-high'),
    ('atomicstrata/llm-wiki-compiler', 'raw/github/llm-wiki-compiler-repo-readme.md', 'medium-high'),
    ('langchain-ai/context_engineering', 'raw/github/langchain-context-engineering-repo-readme.md', 'medium-high'),
    ('langchain-ai/how_to_fix_your_context', 'raw/github/langchain-how-to-fix-your-context-readme.md', 'medium-high'),
]:
    try:
        results.append(gh_readme(owner_repo, rel, reliability=reliability))
    except Exception as e:
        results.append({'path': rel, 'status': 'error', 'error': repr(e)})
    time.sleep(1)

print(json.dumps(results, indent=2))
