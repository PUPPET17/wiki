---
source_url: https://github.com/letta-ai/lettabot/issues/652
fetched_url: https://api.github.com/repos/letta-ai/lettabot/issues/652
source_type: github issue
author: letta-ai/lettabot contributors
source_date: 2026-03-27
ingested: 2026-05-15
sha256: de7404e5cbc4987eecacac17d00678a3a2f40576d35ce13f6b7d350409a0cf9d
raw_preservation: full_github_issue_api_text
extraction_method: github_rest_issue_and_comments
github_repo: letta-ai/lettabot
github_issue: 652
comments_fetched: 0
---

# Letta issue 652: Per-conversation context scoping

## Source Metadata

- Source URL: https://github.com/letta-ai/lettabot/issues/652
- Fetched URL: https://api.github.com/repos/letta-ai/lettabot/issues/652
- Source type: github issue
- Author: letta-ai/lettabot contributors
- Source date: 2026-03-27
- Ingested: 2026-05-15
- Reliability: medium
- Raw preservation status: full_github_issue_api_text
- Extraction method: github_rest_issue_and_comments

## Parsed Source Text

# Feature: Per-conversation context scoping (memfs/block pinning per conversation)

- GitHub issue: https://github.com/letta-ai/lettabot/issues/652
- API URL: https://api.github.com/repos/letta-ai/lettabot/issues/652
- State: open
- Author: ezra-letta
- Created: 2026-03-27T03:02:05Z
- Updated: 2026-03-27T18:37:30Z
- Comments: 0
- Labels: enhancement

## Issue Body

## Problem

All agent context — memfs `system/` files, memory blocks, tools, system prompt — is agent-level and shared identically across every conversation. There's no way to scope context to specific conversations.

This means:
- A shoemaking discussion group sees user profiles for unrelated gaming friends
- A public Discord server gets the same persona details as a private DM
- IoT sensor data conversations load social chat context and vice versa
- Every conversation pays the full token cost of the entire agent's knowledge, regardless of relevance

As agents scale to more conversations across more channels (see #651 for cross-channel conversation routing), this becomes increasingly wasteful and potentially confusing for the agent's attention.

## Current Architecture

| Layer | Scoping | 
|-------|---------|
| Message history | Per-conversation (already isolated) |
| Memfs `system/` files | Agent-level (pinned to ALL conversations) |
| Memory blocks | Agent-level (attached to agent, not conversation) |
| Tools | Agent-level (same toolset everywhere) |
| System prompt | Agent-level (compiled once, same for all) |

## Proposed Capability

Allow specific memfs files or memory blocks to be pinned to specific conversations (or conversation groups from #651):

```yaml
conversations:
  routes:
    gaming-squad:
      - discord:333
      - telegram:ccc
      context:
        include:
          - system/users/gaming-friends.md
          - system/rules/gaming-rules.md
        exclude:
          - system/users/work-contacts.md
    work:
      - discord:444
      context:
        include:
          - system/projects/
          - system/users/work-contacts.md
```

Or alternatively, per-file metadata in memfs:
```yaml
# system/users/gaming-friends.md frontmatter
---
description: Gaming friend group profiles
conversations: [gaming-squad]  # only pinned to this conversation group
---
```

## Implementation Considerations

- System prompt compilation would need to become per-conversation (currently agent-level)
- This is a deeper architectural change than conversation routing (#651)
- May require changes to the Letta server's compilation pipeline, not just LettaBot
- Could start with a simpler version: conversation-level `additionalContext` injection from config, without changing core compilation

## Use Cases

- **Privacy boundaries**: User profiles only visible in conversations where that user participates
- **Attention management**: Agent doesn't get distracted by irrelevant context in focused conversations
- **Token efficiency**: Smaller effective context per conversation = less compaction, lower cost
- **IoT/robotics**: Sensor data schemas only loaded in the relevant control conversation
- **Work/personal separation**: Work project files invisible in social conversations

## Relationship to Other Issues

This builds on #651 (cross-channel conversation routing). Routing defines WHICH chats share a conversation; this defines WHAT context each conversation sees. Both are needed for the full multi-conversation agent experience.

## Comments
