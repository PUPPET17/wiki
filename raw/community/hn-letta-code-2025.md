---
source_url: https://news.ycombinator.com/item?id=46294274
fetched_url: https://hacker-news.firebaseio.com/v0/item/46294274.json
source_type: hn
author: HN: Letta Code
source_date: 2025
ingested: 2026-05-14
sha256: a47c0e51e1230ddb9c9549a6cc8758d9c538fbfb480e7439c6d2003fad5ed6c6
raw_preservation: full_hn_api_thread_text
extraction_method: hacker_news_firebase_api_recursive_comments
hn_item_id: 46294274
comments_fetched: 37
parsed_chars: 17797
---

# Letta Code

## Source Metadata

- Source URL: https://news.ycombinator.com/item?id=46294274
- Fetched URL: https://hacker-news.firebaseio.com/v0/item/46294274.json
- Source type: hn
- Author: HN: Letta Code
- Source date: 2025
- Ingested: 2026-05-14
- Reliability: medium
- Raw preservation status: full_hn_api_thread_text
- Extraction method: hacker_news_firebase_api_recursive_comments

## Parsed Source Text

# Letta Code

- HN item id: 46294274
- URL: https://news.ycombinator.com/item?id=46294274
- Linked URL: https://www.letta.com/blog/letta-code
- By: ascorbic
- Score: 83
- Descendants/comments: 37
- Comments fetched: 37
- Time: 1765918287

## Comments

### Comment 46295362 by pacjam depth=0 time=1765923332

Thanks for sharing!! (Charles here from Letta) The original MemGPT (the starting point for Letta) was actually an agent CLI as well, so it's fun to see everything come full circle.
If you're a Claude Code user (I assume much of HN is) some context on Letta Code: it's a fully open source coding harness (#1 model-agnostic OSS on Terminal-Bench, #4 overall).
It's specifically designed to be "memory-first" - the idea is that you use the same coding agents perpetually, and have them build learned context (memory) about you / your codebase / your org over time. There are some built-in memory tools like `/init` and `/remember` to help guide this along (if your agent does something stupid, you can 'whack it' with /remember). There's also a `/clear` command, which resets the message buffer, but keeps the learned context / memory inside the context window.
We built this for ourselves - Letta Code co-authors the majority of PRs on the letta-code GitHub repo. I personally have been the same agent for ~2+ weeks (since the latest stable build) and it's fun to see its memory become more and more valuable over time.
LMK if you have any q's! The entire thing is OSS and designed to be super hackable, and can run completely locally when combined with the Letta docker image.

### Comment 46297700 by shortlived depth=1 time=1765939930

I'm very interested in trying this out! I run Claude Code in sandbox with `--dangerously-skip-permissions`.  Is that possible with Letta?

### Comment 46297718 by pacjam depth=2 time=1765940111

Yes! Letta Code also has a "danger" mode, it's `--yolo`. If you're running Claude Code in a sandbox in headless mode, Letta Code has that too, just do something like `letta -p "Do something dangerous (it's just a sandbox, after all)" --yolo`
More on permissions here:
https://docs.letta.com/letta-code/permissions
Install is just `npm install -g @letta-ai/letta-code`

### Comment 46303098 by bazhand depth=1 time=1765994553

How does the memory scale (or not!) over time. If using Letta in a single agent mode, similar to just using claude - how does memory blocks stay relevant and contextual?
I guess what I'm asking is, if there is a memory block limit, is that an issue for self learning over time. Claude as you know just straight up ignores CLAUDE.md and doesnt self-improve it.

### Comment 46296150 by koakuma-chan depth=1 time=1765927524

Why can't I see Cursor on tbench? Is it that bad that it's not even on the leaderboard? I am trying to figure out if I can pitch your product to my company, and whether it is worth it.

### Comment 46296258 by pacjam depth=2 time=1765928248

Not sure why Cursor CLI isn't on the leaderboard... I'm guessing it's because Cursor is focused primarily on their IDE agent, not their CLI agent, and Terminal-Bench is an eval/benchmark for CLI agents exclusively.
If you're asking about why Letta Code isn't on the leaderboard, the TBench maintainers said it should be up later today (so probably refresh in a few hours!). The results are already public, you can see them on our blog (graphs linked in the OP). They are also verifiable, all data is available for the runs + Letta Code is open source, so you can replicate the results yourself.

### Comment 46296278 by koakuma-chan depth=3 time=1765928398

I mean, I understand that this is a
terminal
benchmark, but the point is to benchmark LLM harnesses, and whether the output is printed to the terminal, or displayed in the UI shouldn't matter. Are there alternative benchmarks where I can see how Letta Code performs compared to cursor?

### Comment 46296429 by pacjam depth=4 time=1765929359

Ah gotcha! In that case, I think Terminal-Bench is currently the best proxy for "how good is this harness+agent combo at coding (quantitatively)" question. I think it used to be SWE-Bench, but I think T-Bench is a better proxy for this now. Like you said though, unfortunately Cursor isn't listed (probably their choice to not list it, maybe because it doesn't place highly).

### Comment 46296732 by koakuma-chan depth=5 time=1765931546

Alright, I will try out Letta Code manually later then.

### Comment 46296814 by pacjam depth=6 time=1765932280

Cool, let us know what you think! Would recommend trying w/ Sonnet/Opus 4.5 or GPT-5.2 (those are the daily drivers we use internally w/ Letta Code)

### Comment 46295734 by tigranbs depth=0 time=1765925191

In my experience, "memory" is really not that helpful in most cases. For all of my projects, I keep the documentation files and feature specs up to date, so that LLMs are always aware of where to find what and which coding style guides the project is based on.
Maintaining the memory is a considerable burden, and make sure that simple "fix this linting" doesn't end up in the memory, as we always fix that type of issue in that particular way. That's also the major problem I have with ChatGPT's memory: it starts to respond from the perspective of "this is correct for this person".
I am curious who sees the benefits of the memory in coding? Is it like "learns how to code better" or it learns "how the project is structured". Either way, to me, this sounds like an easy project setup thing.

### Comment 46295866 by pacjam depth=1 time=1765925840

I think it cuts both ways - for example I've definitely had the experience where when typing into ChatGPT I know ahead of time that whatever "memory" they're storing and injecting is likely going to degrade my answer, so I hop over to incognito mode. I've also had the experience where I've had a loosely related follow-up question to something and I didn't want to dig through my chat history to find the exact convo, so it's nice to know that ChatGPT will probably pull the relevant details into context.
I think similar concepts apply to coding - in some cases, you have all the context you need up front (good coding practices help with this), but in many cases, there's a lot of "tribal knowledge" scattered across various repos that a human vet working in the org would certainly know, but an agent wouldn't (of course, there's somewhat of a circular argument here that if the agent eventually learned this tribal knowledge, it could just write it down into a CLAUDE.md file ;)). I think there's also a clear separation between procedural knowledge and learned preferences, the former is probably better represented as skills committed to a repo, vs I view the latter more as a "system prompt learning" problem.

### Comment 46296174 by DrSiemer depth=1 time=1765927685

ChatGPTs implementation of Memory is terrible. It quickly fills up with useless garbage and sometimes even plain incorrect statements, that are usually only relevant to one obscure conversation I had with it months ago.
A local, project specific llm.md is absolutely something I require though. Without that, language models kept on "fixing" random things in my code that it considered to be incorrect, despite comments on those lines literally telling it to NOT CHANGE THIS LINE OR THIS COMMENT.
My llm.md is structured like this:
- Instructions for the LLM on how to use it
- Examples of a bad and a good note
- LLM editable notes on quirks in the project
It helps a lot with making an LLM understand when things are unusual for a reason.
Besides that file, I wrap every prompt in a project specific intro and outro. I use these to take care of common undesirable LLM behavior, like removing my comments.
I also tell it to use a specific format on its own comments, so I can make it automatically clean those up on the next pass, which takes care of most of the aftercare.

### Comment 46296456 by pacjam depth=2 time=1765929507

I'm curious - how do you currently manage this `llm.md` in the tooling you use? E.g., do you symlink `AGENTS/CLAUDE.md` to `llm.md`? Also, is there any information you duplicate across your project-specific `llm.md` files that could potentially be shared globally?

### Comment 46307101 by DrSiemer depth=3 time=1766014503

The way I work with LLMs is a bit different.
I use a custom tool, that basically merges all my code into a single prompt. Most of my projects are relatively small, usually maxing out at 200k tokens, so I can just dump the whole thing into Gemini Pro for every feature set I am working on. It's a more manual way of working, but it ensures full control over the code changes.
For new projects I usually just copy the llm.md from the tool itself and strip out the custom part. I might add creating it as a feature of the tool in the future.
A few days ago I tried to use AntiGravity (on default settings) and that was an awful experience. Slow, pondering, continuously making dumb mistakes, only responding to feedback with code and it took at least 3 hours (and a lot of hand holding) to end up on a broken version of what I wanted.
I gave up, tried again using my own tool and was done in half an hour. Not sure if it will work as well for other people, but it definitely does for me.

### Comment 46295902 by wooders depth=1 time=1765926060

I think the problem with ChatGPT / other RAG-based memory solutions is that it's not possible to collaborate with the agent on what it's memory should look like - so it makes sense that its much easier to just have a stateless system and message queue, to avoid mysterious pollution. But Letta's memory management is primarily text/files based so very transparent and controllable.
An example of how this kind of memory can help is learned skills
https://www.letta.com/blog/skill-learning
- if your agent takes the time to reflect/learn from experience and create a skill, that skills is much more effective at making it better next time than just putting the raw trajectory into context.

### Comment 46295789 by danieltanfh95 depth=1 time=1765925434

context poisoning is a real problem that these memory providers only make worse.

### Comment 46295881 by pacjam depth=2 time=1765925936

IMO context poisoning is only fatal when you can't see what's going on (eg black box memory systems like ChatGPT memory). The memory system used in the OP is fully white box - you can see every raw LLM request (and see exactly how the memory influenced the final prompt payload).

### Comment 46296556 by handfuloflight depth=3 time=1765930265

That's significant, you can improve it in your own environment then.

### Comment 46296585 by pacjam depth=4 time=1765930498

Yeah exactly - it's all just tokens that you have full control over (you can run CRUD operations on). No hidden prompts / hidden memory.

### Comment 46295595 by ascorbic depth=0 time=1765924541

Void is the greatest ad for Letta. I'm interested to see if it's as good at coding as it is at posting.
https://bsky.app/profile/void.comind.network

### Comment 46297163 by jamilton depth=1 time=1765935123

What do you like about Void? It reads about how I would expect a base chat model to post.

### Comment 46298981 by ascorbic depth=2 time=1765954329

It's the replies that are the interesting bit. It's not perfect, but it can maintain multiple conversations with different people in the same context, and do things like changing its current rules in response to conversations with users. Its slightly robotic tone is deliberate: it tries to convey information in the most efficient way possible. I'm not sure if that's an emergent property or if its in one of its fixed memory blocks. I do know that earlier on people managed to convince it to change its personality and cpfiffer had to intervene to stop people doing that.

### Comment 46297600 by Retr0id depth=2 time=1765939100

These kind of LLM bots can be fun to play with in a "try to make it say/do something silly" way, but beyond that I don't really get the point. The writing style is grating and I don't think I've ever seen one say anything genuinely useful.

### Comment 46295619 by pacjam depth=1 time=1765924657

I think Cameron (Void's handler) has some experience wiring up production Void to his computer via Letta Code

### Comment 46295659 by cpfiffer depth=2 time=1765924808

I do have some experience but haven't deployed Void on actual tasks, mostly because I want to keep Void focused on day-to-day social operations. I have considered giving Void subagents to handle coding tasks, which may be a good use case for Void-2:
https://bsky.app/profile/void-2.comind.network

### Comment 46295725 by pacjam depth=3 time=1765925132

One cool option is having Void-2 run inside the Letta Code harness (in headless mode) on a sandbox to let is have free access over a computer, just to see what it will do while also connected to bluesky

### Comment 46295813 by jstummbillig depth=0 time=1765925555

I find the long-term memory concepts with regards to AI curiously dubious.
On first glance, of course it's something we want. It's how we do it, after all! Learning on the job is what enables us to do our jobs and so many other things.
On the other hand humans are frustratingly stuck in their ways and not all that happy to change and that is something that societies or orgs fight a lot. Do I want to convince my coding agent to learn new behavior, conflicting with existing memory?
It's not at all obvious to me in how far memory is a bug or a feature. Does somebody have a clear case on why this is something that we should want and why it's not a problem?

### Comment 46295912 by pacjam depth=1 time=1765926107

> Does somebody have a clear case on why this is something that we should want
For coding agents, I think it's clear that nobody wants to repeat the same thing over an over again. If a coding agent makes a mistake once (like `git add .` instead of manually picking files), it should be able to "learn" and never make the same mistake again.
Though I definitely agree w/ you that we shouldn't aspire to 1:1 replicate human memory. We want to be able to make our machines "unlearn" easily when needed, and we also want them to be able to "share" memory with other agents in ways that simply isn't possible with humans (until we all get neuralinks I guess)

### Comment 46296071 by skybrian depth=0 time=1765927007

There are a variety of possible memory mechanisms including simple things recording a transcript (as a chatbot does) or having the LLM update markdown docs in a repo. So
having
memory isn't interesting. Instead, my question is: what does Letta's memory look like? Memory is a data structure. How is it structured and why is that good?
I'd be interested in hearing about how this approach compares with Beads [1].
[1]
https://github.com/steveyegge/beads

### Comment 46296305 by pacjam depth=1 time=1765928519

Beads looks cool! I haven't tried it, but as far as I can tell, it's more of a "linear for agents" (memory as a tool), as opposed to baking long-term memory into the harness itself. In many ways, CLAUDE.md is a weak form of "baking memory into the harness", since AFAIK on bootup of `claude`, the CLAUDE.md gets "absorbed" and pinned in the system prompt.
Letta's memory system is designed off the MemGPT reference architecture, which is intentionally very simple - break the system prompt up into "memory blocks" (all pinned to the context window, since they are injected in system, which are modifiable via memory tools (the original MemGPT paper is still a good reference for what this looks like at a high level:
https://research.memgpt.ai/
). So it's more like a "living CLAUDE.md" that follows your agent around wherever it's deployed - ofc, it's also interoperable with CLAUDE.md. For example, when you boot up Letta Code and run `/init`, it will scan for AGENTS.md/CLAUDE.md, and will ingest the files into its memory blocks.
LMK if you have any other questions about how it works happy to explain more

### Comment 46296960 by handfuloflight depth=2 time=1765933470

Could Beads be additive to Letta's memory? Or could you anticipate conflict or confusion paths?

### Comment 46297734 by pacjam depth=3 time=1765940249

I think it's mostly complimentary, in the same way a linear MCP would be complementary to a MemGPT/Letta-style memory system
I guess the main potential point of confusion would arise if it's not clear to the LLM / agent which tool should be used for what. E.g. if you tell your agent to use Letta memory blocks as a scratchpad / TODO list, that functionality overlaps with Beads (I think?), so it's easy to imagine the agent getting confused due to stale data in either location. But as long as the instructions are clear about what context/memory to use for what task, it should be fine / complementary.

### Comment 46297779 by handfuloflight depth=4 time=1765940685

Great response, thank you. Will experiment then with projects that have already initialized Beads.

### Comment 46298442 by KingMob depth=0 time=1765947630

Bit of a tangent, but what's the codec used in your first video,
https://iasi9yhacrkpgiie.public.blob.vercel-storage.com/lett...
?
Firefox says it can't play it.
I'd download and check it with ffprobe, but direct downloads seem blocked.

### Comment 46299499 by pacjam depth=1 time=1765959861

Oh interesting - it's just a .mp4. I put it on vercel blob storage just as a fast way to make it easily embeddeded in our CMS system, but I think I put it on the wrong Vercel account and the bucket got rate limited (happened a few hours ago, which is when I think you were probably looking). Can you see it now? In my own Firefox it looks OK now.

### Comment 46308902 by KingMob depth=2 time=1766032164

Ahh, maybe that was it. It's playing now. Sorry.
