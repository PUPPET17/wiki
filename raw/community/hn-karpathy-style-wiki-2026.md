---
source_url: https://news.ycombinator.com/item?id=47899844
fetched_url: http://hn.algolia.com/api/v1/items/47899844
source_type: hn
author: HN / WUPHF submitter
source_date: 2026
ingested: 2026-05-14
sha256: 4b41259f34da4d3395597efce51fc1c566577347ff0f133b7395c5b9f077f075
raw_preservation: full_hn_algolia_thread_text
extraction_method: hn_algolia_items_api_recursive_comments
hn_item_id: 47899844
comments_fetched: 115
parsed_chars: 49848
---

# HN: A Karpathy-style LLM wiki your agents maintain (Markdown and Git)

## Source Metadata

- Source URL: https://news.ycombinator.com/item?id=47899844
- Fetched URL: http://hn.algolia.com/api/v1/items/47899844
- Source type: hn
- Author: HN / WUPHF submitter
- Source date: 2026
- Ingested: 2026-05-14
- Reliability: medium
- Raw preservation status: full_hn_algolia_thread_text
- Extraction method: hn_algolia_items_api_recursive_comments

## Parsed Source Text

# Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown and Git)

- HN item id: 47899844
- URL: https://news.ycombinator.com/item?id=47899844
- Author: najmuzzaman
- Points: 260
- Children/comments reported: 36 top-level

## Comments

### Comment 47899922 by dhruv3006 depth=0 created=2026-04-25T09:08:33.000Z

I love that so many people are building with markdown !
But also would like to understand how markdown helps in durability - if I understand correctly markdown has a edge over other formats for LLMs.
Also I too am building something similar on markdown which versions with git but for a completely different use case :
https://voiden.md/

### Comment 47900173 by left-struck depth=1 created=2026-04-25T10:05:37.000Z

I read the durability thing as markdown files are very open, easy to find software for, simple and are widely used. All of this together almost guarantees that they will he viewable/usable in the far future.

### Comment 47900313 by dhruv3006 depth=2 created=2026-04-25T10:32:07.000Z

So markdown will be great for distribution in the future.

### Comment 47902173 by kaoD depth=1 created=2026-04-25T15:25:20.000Z

I'm interested. At a glance this sounds a lot like Hurl[0]. What's the difference?
[0]
https://hurl.dev/

### Comment 47908212 by dhruv3006 depth=2 created=2026-04-26T07:35:23.000Z

I think for hurl you are simply running/asserting apis.
Voiden is for api design,reusability, documentation, and has markdown simplicity - and you can also do pre and post scripts and assertions too!

### Comment 47899960 by goodra7174 depth=0 created=2026-04-25T09:14:34.000Z

I was looking for something similar to try out. Cool!

### Comment 47899966 by davedigerati depth=0 created=2026-04-25T09:15:42.000Z

why not an Obsidian vault with a plugin?

### Comment 47899972 by davedigerati depth=1 created=2026-04-25T09:17:14.000Z

srsly tho this looks slick & love the office refs / will go play with it :)

### Comment 47900475 by frrandias depth=2 created=2026-04-25T11:09:59.000Z

Awesome, let us know if there's any features you want/bugs you hit :)

### Comment 47900097 by tomtomistaken depth=1 created=2026-04-25T09:46:39.000Z

what plugin are you using?

### Comment 47901876 by najmuzzaman depth=1 created=2026-04-25T14:41:00.000Z

Two structural reasons.
1. Obsidian is a single-user editor. It does not have the concept of "agent A drafted this, agent B promoted it, the team approved it." The promotion flow needs a state machine that lives outside the editor. a plugin can simulate it but the source-of-truth has to be a process the agents talk to instead of a vault file.
2. Agents need an MCP surface. An Obsidian plugin API won't do. /lookup, entity_fact_record, notebook_write, and team_wiki_promote are MCP tools the agent runtimes call directly. Obsidian's plugin API targets human users and the Electron app. You would be reimplementing the MCP layer to bridge.
Practical compatibility: you can absolutely point Obsidian at ~/.wuphf/wiki/ and use it as a vault (we got someone from our Reddit post do this). Obsidian can be reader while WUPHF stays the writer.

### Comment 47903076 by kid64 depth=1 created=2026-04-25T17:33:40.000Z

He presumably wanted the result to be good.

### Comment 47899990 by mellosouls depth=0 created=2026-04-25T09:21:05.000Z

Karpathy's original post for context:
https://x.com/karpathy/status/2039805659525644595
https://xcancel.com/karpathy/status/2039805659525644595

### Comment 47900002 by hyperionultra depth=0 created=2026-04-25T09:24:40.000Z

[flagged]

### Comment 47900014 by spiderfarmer depth=1 created=2026-04-25T09:27:27.000Z

Probably just envy.

### Comment 47900070 by wiseowise depth=2 created=2026-04-25T09:39:34.000Z

Obviously it is envy, and not scepticism over a guy who practically lives on Twitter and has unhinged[1] follower base.
1 -
https://x.com/__endif/status/2039810651120705569

### Comment 47903083 by kid64 depth=3 created=2026-04-25T17:34:48.000Z

That's a 404

### Comment 47900045 by William_BB depth=1 created=2026-04-25T09:33:34.000Z

I have the same feeling ever since his infamous LLM OS post

### Comment 47900073 by mirekrusin depth=1 created=2026-04-25T09:40:33.000Z

Feels like disliking musician for fanaticism towards musical instruments.

### Comment 47900034 by jimmypk depth=0 created=2026-04-25T09:30:36.000Z

The BM25-first routing bet is interesting. You mention 85% recall@20 on 500 artifacts, but the heuristic classifier routing "short lookups to BM25 and narrative queries to cited-answer" raises a practical question: what does the classifier key on to decide a query is narrative vs short? Token count? Syntactic structure? The reason I ask is that in agent-generated queries, the boundary is often blurry - an agent doing a dependency lookup might issue a surprisingly long, well-formed sentence. If the classifier routes those to the more expensive cited-answer loop it could negate the latency advantage of BM25 being first.

### Comment 47900497 by tomjwxf depth=1 created=2026-04-25T11:14:04.000Z

Re classifier routing: text-shape signals (token count, syntactic markers) underspecify the boundary, especially for agent-generated queries. The signal that worked better in our policy-gated tool-call setting was the surrounding intent context the agent was operating under, not the query string itself. An agent in a "fact-check" context emits long, well-formed sentences that actually want exact-match retrieval; an agent in an "open research" context emits surprisingly short queries that need narrative retrieval. If the runtime can read the tool or skill context at query time, routing on that is less ambiguous than text shape. Doesn't help if the wiki is a black-box MCP server with no caller-side context, but it's worth offering an optional context hint in the lookup payload.

### Comment 47900083 by Unsponsoredio depth=0 created=2026-04-25T09:43:38.000Z

love the bm25-first call over vector dbs. most teams jump to vectors 
before measuring anything

### Comment 47900176 by armcat depth=0 created=2026-04-25T10:06:21.000Z

Any particular reason for BM25? Why not just a table of contents or index structure (json, md, whatever) that is updated automatically and fed in context at query time? I know bag of words is great for speed but even at 1000s of documents, the index can be quite cheap and will maximise precision

### Comment 47901295 by 0123456789ABCDE depth=1 created=2026-04-25T13:09:45.000Z

do you want to pollute the context with blurbs for docs in disparate topics? cascade filtering, even with naïve bm25, helps reduce the amount of _noise_ that's pushed into the context window. if we reduce the amount of results to consider, further filtering or reranking, with more expensive options, becomes realistic. one could even put a cheaper model in front to further clean the results.

### Comment 47900185 by imafish depth=0 created=2026-04-25T10:08:05.000Z

Cool idea. But is anyone actually building real stuff like this with any kind of high quality?
Every time I hear someone say "I have a team of agents", what I hear is "I'm shipping heaps of AI slop".

### Comment 47900338 by hansmayer depth=1 created=2026-04-25T10:34:35.000Z

+100 for this comment.

### Comment 47900558 by frrandias depth=1 created=2026-04-25T11:23:05.000Z

Hey, contributor to Wuphf here,
We have been using it as a sounding board. I think that in its current state it's actually more useful for someone to learn about how to run a business - "what does a CEO vs PM do" and/or learn about the pros/cons of running a bunch of agents at once.

### Comment 47900622 by jbjbjbjb depth=1 created=2026-04-25T11:34:47.000Z

I remember the personal wiki was a bit of trend 5 years ago but it kind of died because it had an unclear purpose for the most part. I kept one but never really referred to any of the notes and then just went back to a paper and to do list. I’m sure this is useful for those who kept up the habit.

### Comment 47902896 by najmuzzaman depth=2 created=2026-04-25T17:07:13.000Z

this is not a personal wiki though. it is a team wiki. agents are responsible to manage it and keep it fresh and always visible with human oversight.
tbh this won't be much useful as a personal wiki.

### Comment 47900637 by psanchez depth=1 created=2026-04-25T11:37:38.000Z

Even though I did not know about Andrej Karpathy's tweet from earlier this month, I ended up converging on something very similar.
A couple of weeks ago I built a git-based knowledge base designed to run agents prompts on top of it.
I connected our company's ticketing system, wiki, GitHub, jenkins, etc, and spent several hours effectively "onboarding" the AI (I used Claude Opus 4.6). I explained where to find company policies, how developers work, how the build system operates, and how different projects relate to each other.
In practice, I treated it like onboarding a new engineer: I fed it a lot of context and had it organize everything into AI-friendly documentation (including an AGENTS.md). I barely wrote anything myself, mostly I just instructed the AI to write and update the files, while I guided the overall structure and refactored as needed.
The result was a git-based knowledge base that agents could operate on directly. Since the agent had access to multiple parts of the company, I could give high-level prompts like: investigate this bug (with not much context), produce a root cause analysis, open a ticket, fix it, and verify a build on Jenkins. I did not even need to have the repos locally, the AI would figure it out, clone them, analyze, create branches using our company policy, etc...
For me, this ended up working as a multi-project coordination layer across the company, and it worked much better than I expected.
It wasn't all smooth, though. When the AI failed at a task, I had to step in, provide more context, and let it update the documentation itself. But through incremental iterations, each failure improved the system, and its capabilities compounded very quickly.

### Comment 47901061 by dominotw depth=2 created=2026-04-25T12:47:22.000Z

how is this related to parent comment . slop.

### Comment 47902280 by psanchez depth=3 created=2026-04-25T15:43:14.000Z

Well, my comment was meant as an example of a setup for actually building something real with reasonable quality. I was answering to that part of the previous comment.
In my experience, the difference is context. Agents without structure produce slop, but with a well-curated knowledge base and iteration, they can be useful. I was just sharing a setup that has been working for me lately.
Edit: minimal changes for clarity

### Comment 47900675 by stavros depth=1 created=2026-04-25T11:44:30.000Z

The problem with your comment is that the word "real" is just there to move the goalposts. There are people building high-quality stuff like this, yes.
I built a tiny utility like this that works very well yesterday:
https://github.com/skorokithakis/gnosis

### Comment 47902879 by najmuzzaman depth=1 created=2026-04-25T17:05:03.000Z

let's talk about real stuff. we built an AI-native CRM backed by HubSpot founder Dharmesh Shah last year before this, had revenue, iterated to focus on context graph infra which looked like the right moat to focus on, did enterprise PoCs, and all of that distilled into this personal project i built on the side to help my own work. turned out to be right interface for making context infra usable.
the team is of 4 HubSpotters who built HubSpot's largest platforms - search, nav, notifs, permissions, AI.
we are in the process of opening up large pieces of our enterprise context architecture to WUPHF and also ship the cloud enterprise version of WUPHF (
https://nex.ai/new-home
).

### Comment 47900197 by portly depth=0 created=2026-04-25T10:09:58.000Z

I don't understand the point of automating note taking. It never worked for me to copy paste text into my notes and now you can 100x that?
The whole point of taking notes for me is to read a source critically, fit it in my mental model, and then document that. Then sometimes I look it up for the details. But for me the shaping of the mental model is what counts

### Comment 47900373 by _zoltan_ depth=1 created=2026-04-25T10:41:11.000Z

Then you have never worked at a large enough codebase or across enough many projects?

### Comment 47902420 by Bridged7756 depth=2 created=2026-04-25T15:59:46.000Z

It all boils down to the same thing. Work out a system that makes you function. It's as simple as a PKMS of your liking, the problem is that people are allergic to writing their thoughts down.

### Comment 47900375 by stingraycharles depth=1 created=2026-04-25T10:41:17.000Z

The few scientific studies out there actually show a
degradation
of output quality when these markdown collections are fully LLM maintained (opposed to an increase when they’re human maintained), which I found fascinating.
I think the sweet spot is human curation of these documents, but unsupervised management is never the answer,
especially
if you don’t consciously think about debt / drift in these.

### Comment 47900417 by criley2 depth=2 created=2026-04-25T10:53:31.000Z

Are you referring to the one (1) study that showed that when cheaper LLM's auto-generated an AGENTS.md, it performed more poorly than human editted AGENTS.md?
https://arxiv.org/abs/2602.11988
I'd love to see other sources that seek to academically understand how LLM's use context, specifically ones using modern frontier models.
My takeaway from these CLAUDE.md/AGENTS.md efforts isn't that agents can't maintain any form of context at all, rather, that bloated CLAUDE.md files filled with data that agents can gather on the spot very quickly are counter-productive.
For information which cannot be gathered on the spot quickly, clearly (to me) context helps improve quality, and in my experience, having AI summarize some key information in a thread and write to a file, and organize that, has been helpful and useful.

### Comment 47902795 by saadn92 depth=2 created=2026-04-25T16:51:32.000Z

I've been running a variation of this for ~6 months. What seems to work: a background process that reads conversation transcripts after sessions end and then extracts decisions/rejected approaches into structured markdown. I review before I promote it into the context.

### Comment 47900405 by mplappert depth=1 created=2026-04-25T10:48:42.000Z

I think there‘s a serious issue with people using AI to do an immense amount of busywork and then never look at it again. Colossal waste.

### Comment 47900508 by simsla depth=2 created=2026-04-25T11:16:29.000Z

Everyone is writing. Nobody is reading.

### Comment 47900888 by mohamedkoubaa depth=3 created=2026-04-25T12:25:29.000Z

In my over a decade of experience as a software engineer, writing code was always a smaller fraction of my time compared to reading code, debating code with colleagues, and wrangling ops. Optimizing for velocity of writing code will inevity lead to spaghetti at best and vaporware at worst.

### Comment 47901069 by danielbln depth=4 created=2026-04-25T12:47:42.000Z

There is also discussion, ping pong with the agent, exploring parallel paths, quickly experimenting, analyzing code, researching things. A code agent can do more than "write me as much code as possible, go!".

### Comment 47902386 by mohamedkoubaa depth=5 created=2026-04-25T15:55:15.000Z

That's how I use agents, but I see less experienced engineers brag about how much code they pump out and it makes me cringe

### Comment 47903721 by rafaelmn depth=4 created=2026-04-25T19:08:23.000Z

I feel like this take misses what LLMs actually bring to the table to a senior developer.
Sure writing code was not the majority of my workday since I moved up in responsibility chain - but that's because I don't get enough uninterrupted time to do the actual coding from all the meetings, syncs, planning, production investigations, mentoring, team activities.
Now that I can delegate code writing to LLM instead of mid/junior devs the dynamics of those tasks change dramatically. The overhead of managing more junior devs is completely gone and no need to have soft skills with an LLM. And communication/iteration speed with LLM is not comparable.
Not to mention I don't need soo much time to get back "into the zone" - LLM can keep working through my meeting - when I'm back it's already working on something and I can quickly get back into the gist of it - much faster than before when I had to take a break and lost all context of what I was doing an hour later. LLM has all that context + more progress right there.
After soo many years of dev I have a pretty good idea of what I want the code to look like - no need to debate the overzealous mid dev about his over abstracted system that's going to haunt me in a production outage next month when we both forgot what he put in - I simply get to say "this is shit rewrite it how I requested". No need to "talk about latest lib that's all the rage on the YouTube blogs etc."
Sure sometimes I realize that doing stuff without LLM would have taken less time - but when I consider how many interruptions I have between my coding sessions - LLMs are empowering precisely because I get to dedicate so little time to my code.
Also less teammates means less communication overhead.

### Comment 47904021 by skybrian depth=3 created=2026-04-25T19:48:57.000Z

The LLM's do quite a lot of reading. The question is what to feed them. (What counts as good context?)

### Comment 47902631 by 4b11b4 depth=2 created=2026-04-25T16:28:37.000Z

It's almost akin to eating without thinking... just a waste, no nutrition. Additionally, damaging.

### Comment 47903741 by nicbou depth=2 created=2026-04-25T19:11:26.000Z

It's such a promising technology, but it seems like the primary use case is to drown everything in noise.

### Comment 47900428 by frocodillo depth=1 created=2026-04-25T10:57:16.000Z

First of all, this is more than just note taking. It appears to be a (yet another) harness for coordinating work between agents with minimal human intervention. And as such, shouldn’t part of the point be to not have to build that mental model yourself, but rather offload it to the shared LLM “brain”?
Highly debatable whether it’s possible to create anything truly valuable (valuable for the owner of the product that is) with this approach, though. I’m not convinced that it will ever be possible to create valuable products from just a prompt and an agent harness. At that point, the product itself can be (re)created by anyone, product development has been commodified, and the only thing of value is tokens.
My hypothesis is that “do things that don’t scale”[0] will still apply well into the future, but the “things that don’t scale” will change.
All that said, I’ve finally started using Obsidian after setting up some skills for note taking, researching, linking, splitting, and restructuring the knowledge base. I’ve never been able to spend time on keeping it structured, but I now have a digital secretary that can do all of the work I’m too lazy to do. I can just jot down random thoughts and ideas, and the agent helps me structure it, ask follow-up questions, relate it to other ongoing work, and so on.  I’m still putting in the work of reading sources and building a mental model, but I’m also getting high-quality notes almost for free.
[0]:
https://www.paulgraham.com/ds.html

### Comment 47900756 by frrandias depth=2 created=2026-04-25T11:58:40.000Z

Hey, one of the contributors to Wuphf here
I think your take is right. This isn't going to help with the internalization of knowledge that note taking will get you. I do think that there is some value in the way we've set up blueprints of agents if you haven't set up a business before to either teach about role functions in a business or get a head start on business that doesn't create something new. At the very least it's a quick setup to getting to experiment.
To the part about note taking (and disclosure) - we are working on a context graph product that lessens the work of reading sources, especially over time and breath to help with a lot of the structure you've mentioned.

### Comment 47900760 by bushido depth=2 created=2026-04-25T11:59:45.000Z

If you think of an agent harness as a tool which you use to build your product, then I think you might be absolutely right. I don't see it being easy for a harness to ever build a product.
I actually think that the harnesses which do end up building products, the harness will be the product.
As an example, I have a harness which I have my entire team use consistently. The harness is designed for one thing: to get the results I get with less nuanced understanding of why I get it.
Mind you, most of my team members are non-technical, or at least would be considered non-technical, two years ago.
These days, I spend most of my time fine-tuning the harness. What that gives me is a team which is producing at 5x their capacity from three months ago, and I get easier to review, more robust pull requests that I have more confidence in merging.
It's still a far cry from automating the entire process. I still think humans need to give the outcomes to even the harnesses to produce the results.

### Comment 47900992 by jstummbillig depth=2 created=2026-04-25T12:39:24.000Z

> My hypothesis is that “do things that don’t scale”[0] will still apply well into the future, but the “things that don’t scale” will change.
Say more?

### Comment 47900471 by 0123456789ABCDE depth=1 created=2026-04-25T11:08:47.000Z

i've been running a variation of the _llm writes a wiki_ since late february. i run it on a sprite (sprites.dev from fly.io), it's public but i don't particularly advertise it. i completely vibe coded the shit out of it with claude. the app side and the content. the app side makes the content accessible to other agent instances, lists some documents at the root, provides search function, and let's me read it on a browser with nice typography if i want to, as opposed to raw markdown.
it's neat, i can create a new sprite/whatever, point claude at the root, and tell it to setup zswap and it will know exactly how to do so in that environment. if something changes, and there's some fiddling to make it work, i can ask it to write a report and send it in to fold into the existing docs.

### Comment 47901022 by emsign depth=1 created=2026-04-25T12:42:43.000Z

Man, there's no point in replying. You are argueing with a non-human therefore the conversation is without meaning and impact and thus a waste of time and energy.

### Comment 47901280 by arikrahman depth=1 created=2026-04-25T13:08:25.000Z

I thought this was parody at first as well for a redundant useless product as it was named after the redundant useless product of the same name from The Office (Wuphf.com)

### Comment 47901403 by big_man_ting depth=1 created=2026-04-25T13:23:39.000Z

Totally agree re note taking. We treat our notes way too lightly, just as an attic or a basement leads to hoarding more stuff than you'll ever need.
Most things do not need to end up in your notes, and LLMs add too much noise, one that you likely never personally verify/filter out at all.
JA Westenberg made a good video essay about it a few days ago:
https://youtube.com/watch?v=3E00ZNdFbEk

### Comment 47902451 by Bridged7756 depth=1 created=2026-04-25T16:02:53.000Z

Ditto.
It circles back to the question, is this unimportant enough for me to delegate it to a LLM that might get it wrong? If the answer is yes, why even do it to begin with. If the answer is no, you have to do it manually.
I personally though, see value in this type of automation. Stuff like tag categorization, indexing, that otherwise would've been lost seems like a good fit for LLMs. Whether or not they're an ideal solution and something else like a search engine would've been a better fit, is a different question.

### Comment 47902771 by anuramat depth=1 created=2026-04-25T16:49:04.000Z

been thinking the same, but I imagine you could explicitly separate notes and slop, eg something as simple as cron job that goes through all your notes and creates a PR if there's some easy win: typos, inconsistencies, tags, etc
I've been coding like this lately: if I'm too lazy to review a new non-critical section/unit tests, I'll mark it as `// SLOP`; later, if I have to, I'll go through the entire thing, and unmark
shitty tests are better than no tests, as long as you your expectations are low enough

### Comment 47904191 by adamsmark depth=1 created=2026-04-25T20:10:25.000Z

I use my Openclaw setup to record notes I don't ever want to remember the details of. Here are some examples:
Storing my Health Insurance's Member ID, RxBin and other data.
Recording the serial number of a product I will be calling technical support for.
Organizing files to be more logical and deduplicating or consolidating as needed.
Whenever I want this info, I'll just ask my LLM to pull it up.

### Comment 47904997 by johntash depth=2 created=2026-04-25T22:02:46.000Z

Do you use local models for these, or are you okay with giving private details to anthropic/openai?
(that's one of my biggest hurdles for really adopting any useful assistant type of agent)

### Comment 47956804 by adamsmark depth=3 created=2026-04-30T01:05:16.000Z

I
want
to use local LLMs, and in fact I have enough VRAM (12GB) and RAM (96GB) to do it but I gave up because it was pretty buggy with the Gemma 4 26B (A4B?) Q4 models. It also meant I had to give up local voice transcription because I needed all my VRAM dedicated to the LLM.
The other thing is I will ask an agent via Telegram to code stuff, so I want an agent that is smart enough to do it all. I prefer brute forcing with money right now. I hate when LLM make bizarre mistakes, I end up spending way too much time figuring out the issue.
I use Openrouter, so
hopefully
no one has built a perfect replica of me in their storage. I flip between models too.
But to be clear, I am living dangerously with agentic workflows in general. Haven't been burnt yet (other than accidentally running up a huge Gemini bill which made me switch to Codex Oauth and Openrouter for cheap Minimax 2.7)
I am moving to a commander/orchestrator model to use both frontier and cheap models and eventually a better local LLM once I buy a 5070 Ti, 3090, 64GB Mac M1 Max, 128GB Strix Halo (probably missed that train) or the AMD R9700.

### Comment 47900201 by souravroy78 depth=0 created=2026-04-25T10:10:24.000Z

Don’t know if Karpathy even wrote this version. Where are the citations?

### Comment 47905402 by najmuzzaman depth=1 created=2026-04-25T22:54:35.000Z

karpathy's llm wiki tweet and gist:
https://x.com/karpathy/status/2040470801506541998?s=20
i used this idea to create a version that works for a team of ai agents

### Comment 47907386 by souravroy78 depth=1 created=2026-04-26T04:36:22.000Z

Nice

### Comment 47900222 by batoga depth=0 created=2026-04-25T10:14:19.000Z

Put AI in your product name, make billion dollars. Put Karpathy in your blog article, get hired by Anthropic as Principal engineer. Milk money as long as fad last. No one is thinking about customer needs, everyone is trying to wash hands in the wave as it last.

### Comment 47900533 by girvo depth=1 created=2026-04-25T11:19:52.000Z

Just like NFTs, just like the blockchain before that, in some ways kind of like the Web 2.0 craze (though we at least built some things then and the tight financing at the time kept a lid on it).
This LLM stuff at least has some real possibilities and value, and is very fun tech to learn about and play with.
I long ago accepted that there’s money to be made, as long as it’s not unethical, then get involved. Can build cool things that do have value, while enjoying the VC/PE money sloshing around

### Comment 47900681 by ting0 depth=1 created=2026-04-25T11:45:39.000Z

Hey man, if it works it works. There's a reason everyone is creating AI tools. We're all buying them. I'm still waiting for someone to make a world-class cli harness that can replace Claude Code but solves the memory and design problem. Web design is still a nightmare with LLMs.

### Comment 47901721 by rglover depth=2 created=2026-04-25T14:15:55.000Z

Cline. Works as a CLI and VSCode plugin.

### Comment 47901913 by hmokiguess depth=2 created=2026-04-25T14:45:46.000Z

Could you elaborate on the web design point? I find them excellent at it personally and it’s where I most often get value out of them

### Comment 47902029 by najmuzzaman depth=2 created=2026-04-25T15:03:22.000Z

thanks for saying this. one more reason people are hating on SaaS so much is that the UI is dry and for many, unusable. on the other hand, the cool AI agents have UI which is fun but again, unusable.
fun and usable can co-exist and we are trying the best to prove that. also, we have an amazing designer who never worked at big tech and has no accolades, but man got taste.

### Comment 47901976 by najmuzzaman depth=1 created=2026-04-25T14:56:35.000Z

alright sir/ma'am/neither. we built an AI-native CRM backed by HubSpot founder Dharmesh Shah last year before this, had revenue, iterated to focus on context graph infra which looked like the right moat to focus on, did enterprise PoCs, and all of that distilled into this personal project i built on the side to help my own work. turned out to be right interface for making context infra usable.
not interested in a job at Anthropic as Principal Engineer (i used to be a HubSpot Product Manager with a healthy income, much better than what i am making now, or for the next few years).
took multiple bets and did iterations because we talked to customers and kept evolving while our old competition is still building an AI CRM "in stealth".
been around enough to know waves don't matter but there is still value behind those waves worth extracting away.

### Comment 47900238 by vlady_nyz depth=0 created=2026-04-25T10:18:15.000Z

need to try out asap. love the „the office“ vibe

### Comment 47900272 by dataviz1000 depth=0 created=2026-04-25T10:25:08.000Z

LLM models and the agents that use them are probabilistic, not deterministic. They accomplish something a percentage of the time, never every time.
That means the longer an agent runs on a task, the more likely it will fail the task. Running agents like this will always fail and burn a ton of token cash in the process.
One thing that LLM agents are good at is writing their own instructions. The trick is to limit the time and thinking steps in a thinking model then evaluate, update, and run again. A good metaphor is that agents trip. Don't let them run long enough to trip. It is better to let them run twice for 5 minutes than once for 10 minutes.
Give it a few weeks and self-referencing agents are going to be at the top of everybody's twitter feed.

### Comment 47901410 by iterateoften depth=1 created=2026-04-25T13:24:34.000Z

It’s also that agents and ML reach local maximima unless external feedback is given. So your wiki will reach a state and get stuck there.

### Comment 47901500 by dataviz1000 depth=2 created=2026-04-25T13:41:04.000Z

Here is an iteresting thing.
> "The LLM model's attention doesn't distinguish between "instructions I'm writing" and "instructions I'm following" -- they're both just tokens in context."
That means all these SOTA models are very capable of updating their own prompts. Update prompt. Copy entire repository in 1ms into /tmp/*. Run again. Evaluate. Update prompt. Copy entire repository ....
That is recursion, like Karpathy's autoresearch, it requires a deterministic termination condition.
Or have the prompt / agent make 5 copies of itself and solve for 5 different situations to ensure the update didn't introduce any regressions.
> reach local maximima unless external feedback is given
The agents can update themselves with human permission. So the external feedback is another agent and selection bias of a human. It is close to the right idea. I, however, am having huge success with the external feedback being the agent itself. The big difference is that a recursive agent can evaluate performance within confidence interval rather than chaos.

### Comment 47900347 by hansmayer depth=0 created=2026-04-25T10:36:08.000Z

Couldn't you instruct your LLM to make the starting dir configurable?

### Comment 47905379 by najmuzzaman depth=1 created=2026-04-25T22:52:26.000Z

yes, and we should expose it. today the wiki location is hardcoded to ~/.wuphf/wiki/. making it a config field is a quick change. just filed an issue:
https://github.com/nex-crm/wuphf/issues/310

### Comment 47908818 by hansmayer depth=2 created=2026-04-26T09:28:09.000Z

I mean did you really need someone on HN to tell you that? Makes me wonder what else have you offloaded onto the statistical parrot.

### Comment 47927895 by najmuzzaman depth=3 created=2026-04-27T21:55:08.000Z

nicht geil. are you really so full of yourself? every customization is not "required" from day-1 and is always a (maintenance and UX) disaster if you did. i have filed an issue for it but not added it to the system yet. not gonna AI slop this just for the sake of adding another feature.

### Comment 47900421 by GistNoesis depth=0 created=2026-04-25T10:54:21.000Z

The space of self building artefacts is interesting and is booming now because recent LLM versions are becoming good at it fast (in particular if they are of the "coding" kind).
I've also experimented recently with such a project [0] with minimal dependencies and with some emphasis on staying local and in control of the agent.
It's building and organising its own sqlite database to fulfil a long running task given in a prompt while having access to a local wikipedia copy for source data.
A very minimal set of harness and tools to experiment with agent drift.
Adding image processing tool in this framework is also easy (by encoding them as base64 (details can be vibecoded by local LLMs) and passing them to llama.cpp ).
It's a useful versatile tool to have.
For example, I used to have some scripts which processed invoices and receipts in some folders, extracting amount date and vendor from them using amazon textract, then I have a ui to manually check the numbers and put the result in some csv for the accountant every year. Now I can replace the amazon textract requests by a llama.cpp model call with the appropriate prompt while still my existing invoices tools, but now with a prompt I can do a lot more creative accounting.
I have also experimented with some vibecoded variation of this code to drive a physical robot from a sequence of camera images and while it does move and reach the target in the simple cases (even though the LLM I use was never explicitly train to drive a robot), it is too slow (10s to choose the next action) for practical use. (The current no deep-learning controller I use for this robot does the vision processing loop at 20hz).
[0]
https://github.com/GistNoesis/Shoggoth.db/

### Comment 47900554 by sails depth=0 created=2026-04-25T11:22:48.000Z

How do you anticipate teams deploying this? I’m wary of GitHub for sensitive business documents, and wonder what an easy secure agent friendly deployment looks like. Cloudflare or GCP are maybe good candidates

### Comment 47900774 by frrandias depth=1 created=2026-04-25T12:04:04.000Z

Hey, contributor to Wuphf here,
Right now this is setup to be run on your machine. Git is used to do versioning but we don't push that to GitHub, nor do we keep any insight into what you have or what you're doing.
If there is long term value people are getting out of Wuphf we'll be happy to build out a hosted business/enterprise compliant version.

### Comment 47901017 by sails depth=2 created=2026-04-25T12:41:54.000Z

Thanks. 
I mean self hosting a shared version of this on internal infra but designed to be slightly collaborative.

### Comment 47900949 by RivoLink depth=0 created=2026-04-25T12:35:08.000Z

For everyone working with markdown, I’d like to share leaf with you, a terminal markdown previewer :
https://github.com/RivoLink/leaf

### Comment 47901185 by LanMeng-LM depth=0 created=2026-04-25T13:00:11.000Z

Would be great if the provider layer supported arbitrary OpenAI-compatible endpoints — DeepSeek, for example. Any plans?

### Comment 47902999 by najmuzzaman depth=1 created=2026-04-25T17:22:08.000Z

supported via OpenCode, which is the runtime that speaks the OpenAI-compatible surface. DeepSeek exposes that surface, so the path is: point OpenCode at the DeepSeek base URL and key, then set OpenCode as your synthesis or runtime CLI in the WUPHF config.
can also do llama.cpp server, LM Studio, LocalAI, OpenRouter, Together, Anyscale, and anything else with the OpenAI surface. i am using ollama already through OpenCode.
if you hit a specific endpoint that does not work, please file an issue.

### Comment 47901360 by zby depth=0 created=2026-04-25T13:16:58.000Z

Reviewed:
https://zby.github.io/commonplace/agent-memory-systems/revie...
It is a third llm wiki on front page in 24 hours!
Obviously it is a hot topic. I have my own horse in that race - so I might not be objective - but I've compiled a wishlist for these system:
https://zby.github.io/commonplace/notes/designing-agent-memo...
I wish there was a chance for collaboration - everybody coding their own system seems like a lot of effort duplication.

### Comment 47901981 by frrandias depth=1 created=2026-04-25T14:56:56.000Z

taking a look :)

### Comment 47902057 by Myrmornis depth=1 created=2026-04-25T15:07:11.000Z

Your notes look really interesting, thanks. I'm curious --from the prose style it's clear they were written by an LLM. For  design notes like this do you sort of have a mental TODO to go back and write them up in your own words to make sure they really capture your own opinions?

### Comment 47902136 by zby depth=2 created=2026-04-25T15:18:57.000Z

For the design notes like:
https://zby.github.io/commonplace/notes/designing-agent-memo...
- I iterate over and over to clean them. This one is also a compilation with many intermediate documents.
But the reviews are written automatically - here are the instructions:
https://github.com/zby/commonplace/blob/main/kb/agent-memory...
Overall the knowledgebase is a mixture of these. I have this disclaimer on the first page:
This KB is itself agent-operated: a human directs the inquiry, AI agents draft, connect, and maintain the notes. The framework for building knowledge bases is documented using that framework.
I hope it is enough - I've seen many people get angry with publishing LLM generated work.

### Comment 47902075 by najmuzzaman depth=1 created=2026-04-25T15:10:14.000Z

love the "Borrowable Ideas" section. would suggest to definitely borrow them.
full disclosure: we started as a context infra company (nex.ai) from long long before Karpathy even came up with the LLM wiki idea, and have barely exposed any of that stuff to WUPHF but starting to open some of that now. glad to see the concerns in the comparison are things that our context infra already built for.
still, happy to collab & share learnings, and of course avoid duplication.

### Comment 47902645 by 4b11b4 depth=1 created=2026-04-25T16:30:38.000Z

yes, generative slot machines are isolating. You say you "wish there was a chance"? As if there isn't?

### Comment 47903901 by SOLAR_FIELDS depth=1 created=2026-04-25T19:32:36.000Z

I mean honestly this stuff is now in roll your own territory now. Run QMD on an obsidian vault and that's like 80% of the way there and you can probably do that in < 2 hours

### Comment 47901447 by 410298 depth=0 created=2026-04-25T13:31:31.000Z

I no longer can tell if this is satire or not:
https://wuphf.team/
It looks like gastown. Using AI is like children playing with a dollhouse. If it is satire, well done.

### Comment 47905349 by najmuzzaman depth=1 created=2026-04-25T22:48:32.000Z

had fun while building this and love "The Office". fwiw i used to be a stand up comic and did lots of satire, but this one is not a shell/slop project to take on the craziness of slop agents being shipped as world-changing (while all they did was asked AI to write smart md files).
there is real substance in the product itself and something that i use myself for work. feel free to ask any questions.

### Comment 47901491 by Abby_101 depth=0 created=2026-04-25T13:38:57.000Z

The "garbage facts in, garbage briefs out" caveat is the part I'd want stress tested. In my own LLM features the context that decays fastest is what agents wrote without a human glance. Six months in, you have entries that are confidently wrong and the lint pass can't tell which. Does the promotion flow require human review or can agents self promote?

### Comment 47901587 by GistNoesis depth=0 created=2026-04-25T13:54:41.000Z

Have you seen this one ?
https://www.reddit.com/r/ClaudeAI/comments/1sv7fvc/im_a_nurs...

### Comment 47903983 by genewitch depth=1 created=2026-04-25T19:43:42.000Z

i wanted to take a picture of my PDR - Physician's Desk Reference tomes, but i gave them to my wife to use at work. But, the publisher stopped publishing the PDR on paper and went to "app-only" and requires payment, now. Used to be you could go to those library "used book sales" or university used library book sales and get ones a couple years out of date.
but no longer.
I didn't even have to look at the (reddit op linked) site or an archive to know that it was going to be wrong, dangerous, a liability, and bordering on unethical.

### Comment 47901627 by Invictus0 depth=0 created=2026-04-25T14:00:46.000Z

The title of this post doesn't match the repo at all

### Comment 47902563 by najmuzzaman depth=1 created=2026-04-25T16:18:40.000Z

fair. the post title leads with the wiki because the Karpathy framing is the angle i think this audience cares about, but the wiki ships as part of WUPHF (an open source collaborative office for AI agents) and the repo README naturally leads with the broader product. i should have surfaced "ships as part of WUPHF" earlier in the post body.
if you want the wiki only, install WUPHF and only use the wiki layer. the promotion flow, fact log, and /lookup work without the multi-agent office around them.

### Comment 47901808 by smadam9 depth=0 created=2026-04-25T14:30:48.000Z

A comment here mentioned "Everyone is writing. Nobody is reading." but I think the friction starts even further upstream.
I've been building a native Mac app "Sig" around this idea: capture has to come from you. You sit down after a meeting and articulate what happened — what was decided, who committed to what, what you actually think. That articulation is the work. The AI routes it into files. If you skip that step and scrape transcripts instead, no promotion workflow saves you. You're just contributing to the garbage in, garbage out idea.
That is Sig <
https://news.ycombinator.com/item?id=47901737
>

### Comment 47901854 by mehhehheehh depth=0 created=2026-04-25T14:37:03.000Z

Hacking

### Comment 47901936 by hmokiguess depth=0 created=2026-04-25T14:49:48.000Z

Someone should build a StackOverflow revival as the solution to this, a distributed knowledge graph curated by humans but driven by collective LLMs trying to problem solve their way out of things and stopping to ask questions in an old fashioned way.
I would be fine with my agent saying “hey, we hit a wall here, here’s the question posted on SO, I flagged to come back to it later once we have an answer”

### Comment 47902027 by ryanshrott depth=0 created=2026-04-25T15:03:12.000Z

One practical approach that works is separating the capture layer from the promotion layer. Agents can draft freely, but anything that gets promoted to trusted status needs a human review. Some teams use a voting scheme where multiple agents independently summarize the same source, and you only promote it when they converge. The confidently wrong problem gets worse over time because bad entries get cited by other agents, and that's how you end up with a knowledge base full of confident BS.

### Comment 47915713 by drewbatcheller depth=1 created=2026-04-26T23:01:00.000Z

The "draft freely, promote on approval" method is the only thing I think works. Anything else is open to way too many forms of context poison. And you're either buried in writing safeguards, adding review layers, or you're praying you don't hit edge cases.
You don't have to trust the capture layer. Put a reviewer agent on top with memory of what's been approved and rejected, keep a human in the loop on the close calls. Over time the reviewer gets calibrated and the human review queue shrinks.

### Comment 47903196 by mncharity depth=0 created=2026-04-25T17:50:16.000Z

Just to stir thought, I note the TiddlyWiki[1] community (wiki as a self-modifying single html file; 20+ years old) has of course been exploring AI tooling... though not necessarily as an agentic environment. There's a markdown plugin, and others to make the file executable, or into a self-serving web app. Git is more problematic. So hypothetically, one could have a single-file agentic wiki wandering around and self-editing.
[1]
https://tiddlywiki.com/

### Comment 47908792 by jermolene depth=1 created=2026-04-26T09:23:45.000Z

(Disclosure: I originally created TiddlyWiki.)
For the single-file configuration you describe, there are already several LLM connectors — e.g. [1]. The appeal is exactly what you note: no dependencies, no installation, trivially archivable. A single-file agentic wiki wandering around and self-editing isfeasible today.
For something closer to Karpathy's LLM Wiki pattern, I've been working on twillm[2], which uses TiddlyWiki's Node.js configuration. That setup saves tiddlers as individual files, so you can point it at an existing Markdown vault and work alongside tools like Claude Code.
Some benefits of TiddlyWiki for this:
* Open source, so you can be confident it'll remain usable indefinitely.
* Web-based, so accessible anywhere.
* Computed views replace materialised index files. Karpathy's setup relies on an index.md that the LLM has to keep in sync as it adds notes — something LLMs are bad at, with staleness creeping in across sessions. TiddlyWiki views are live filter expressions: "tiddlers tagged concept, sorted by rating" computes its contents at render time.
* Frontmatter becomes queryable structure. Obsidian renders YAML frontmatter as boxed metadata at the top of a note. TiddlyWiki promotes frontmatter fields into first-class tiddler fields you can filter, sort, and aggregate over.
* LLM-authored applets, not just content. Beyond Markdown notes, the LLM can drop in wikitext tiddlers (.tid) that act as small interactive live views: dashboards, browse-by-tag tools, journal indexes, glossary pages.
[1]
https://github.com/rimir-cc/tw-llm-connect
[2]
https://github.com/Jermolene/twillm

### Comment 47903600 by renan_warmling depth=0 created=2026-04-25T18:48:44.000Z

The idea seems good, but the system lacks snapshots and data enrichment for each file iteration. If the code breaks or has a bug, the agent could roll back the code and generate enrichment explaining the reason for the rollback, thus generating a new snapshot with updated states. Another issue is the weight of opinion: how will you guarantee integrity and consistency throughout the production of an operating system and avoid collisions and violations of business rules? And regarding persisted memory, currently your system doesn't distinguish between temporal and atemporal memory (business rules, software behaviors and functions, security policies, and governance between agents). The idea is good, but to function as a team, this must also be considered.

### Comment 47905066 by johntash depth=0 created=2026-04-25T22:10:02.000Z

How do you keep llms from writing _too much_?   I've built a few similar tools and systems, and they're all way too easy for the llm to just keep documenting things to the point the whole system is a mess and becomes less useful the bigger it gets.
One example experiment I had was seeing if I could get a llm to build its own knowledge wiki where I would paste a few links and have it go do some research on whatever the subject was, then distill what it finds into specific wiki pages with links to other pages or the source refs.  It looked good until you read the actual data.
This was a few years ago though, so maybe it's worth trying again with something like opus 4.7.

### Comment 47906667 by samarthv depth=0 created=2026-04-26T02:15:45.000Z

really good work

### Comment 47906730 by manfre depth=0 created=2026-04-26T02:30:19.000Z

llm-wiki is a popular topic. I've found it to be very helpful with keeping details of the random web pages I visit and want to remember. I create a claude plugin designed to work with Obsidian's Web Clipper and qmd for search.
https://manfre.me/posts/2026/04/build-llm-wiki-obsidian/

### Comment 47908137 by psteinweber depth=0 created=2026-04-26T07:18:27.000Z

I couldn't find out on the fly: does it support multiple humans?
A lot of these tools (paperclip) don't, but for our small, agent-supported team, that would be the feature we're looking for. I.e. the agents of different marketing roles talking to each other, with clearly defined 'human in the loop' decision making.

### Comment 47911793 by michelhabib depth=0 created=2026-04-26T16:59:09.000Z

Just wondering if AI Notes would add value or create noise. I do love the website Ascii style :)

### Comment 47919663 by gbram depth=0 created=2026-04-27T10:02:42.000Z

Checkout out
https://hivemindai.dev
, which is a shared coordination layer for ai agents but can be shared across different users/teams and just captures the main decisions/actions instead of all the junk in between
