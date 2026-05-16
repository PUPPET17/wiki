---
source_url: https://news.ycombinator.com/item?id=37894403
fetched_url: https://hacker-news.firebaseio.com/v0/item/37894403.json
source_type: hn
author: "HN: MemGPT: Towards LLMs as Operating Systems"
source_date: 2023-10-15
ingested: 2026-05-14
sha256: c843f35c82633d579ccd079b4b729b42bcd81a00740c3d98159e4deb35fb9c02
raw_preservation: full_hn_api_thread_text
extraction_method: hacker_news_firebase_api_recursive_comments
hn_item_id: 37894403
comments_fetched: 106
parsed_chars: 39825
---

# MemGPT: Towards LLMs as Operating Systems

## Source Metadata

- Source URL: https://news.ycombinator.com/item?id=37894403
- Fetched URL: https://hacker-news.firebaseio.com/v0/item/37894403.json
- Source type: hn
- Author: HN: MemGPT: Towards LLMs as Operating Systems
- Source date: 2023-10-15
- Ingested: 2026-05-14
- Reliability: medium
- Raw preservation status: full_hn_api_thread_text
- Extraction method: hacker_news_firebase_api_recursive_comments

## Parsed Source Text

# MemGPT: Towards LLMs as Operating Systems

- HN item id: 37894403
- URL: https://news.ycombinator.com/item?id=37894403
- Linked URL: https://arxiv.org/abs/2310.08560
- By: belter
- Score: 225
- Descendants/comments: 106
- Comments fetched: 106
- Time: 1697412795

## Comments

### Comment 37906874 by dang depth=0 time=1697491517

As there is another thread about this currently on the front page, I've merged all the comments that are
not
just bickering about the title into that one:
https://news.ycombinator.com/item?id=37901902

### Comment 37895618 by pacjam depth=0 time=1697426668

Hey all, I’m the lead author on this work. Thanks to the OP for posting, and for all the interest and feedback. To clarify a few points: the goal of this work is to investigate the extent to which an LLM can manage memory and different memory hierarchies, applying lessons from operating systems to extend effective context lengths. All of our code is open sourced at
https://github.com/cpacker/MemGPT
so you can try it out yourselves!

### Comment 37895912 by a1j9o94 depth=1 time=1697430149

This is a fascinating approach! I posted this as a separate comment but would be curious about your response directly.
What do you think about the tradeoff of having an agent manage its own memory as opposed to having a separate agent whose job it is to manage the memory and the other agent just focuses on the conversation?

### Comment 37895916 by pacjam depth=2 time=1697430210

Thanks for your interest! Left a comment on the other thread

### Comment 37906832 by dang depth=3 time=1697491312

That other thread is
https://news.ycombinator.com/item?id=37895861
in case anyone wants it

### Comment 37907159 by sabareesh depth=1 time=1697493036

well basically this is what i have been doing since functions introduced part of chatgpt api

### Comment 37898078 by isatty depth=0 time=1697454365

It’s an interesting paper by credible academics but the name is just downright terrible. I suppose I’m extra annoyed because I don’t really have an interest in LLMs to begin with but I do in operating systems.

### Comment 37904043 by trenchgun depth=1 time=1697480983

It is a horrible name, but probably gets more attention this way. Paper itself seems good.

### Comment 37896241 by skrebbel depth=0 time=1697434625

Sorry if this is a bit meta but why is it so popular and accepted to Just Say Stuff in AI land? Sometimes it seems to me that AI people have begun hallucinating as much as the models they’re training.
This article seems pretty cool but in no way has it anything to do with its title. “Operating system” has a clearly defined meaning and it’s not “a thing that has memory”. To me these kinds of grandiose claims with no substance undermine the credibility of the authors.
I mean what’s wrong with “Tiered memory layers to provide extended AI context windows”?

### Comment 37896831 by lgessler depth=1 time=1697442223

IMO, as an NLP researcher, it's a product of the "fast science" culture of AI where there are more papers than anyone could possibly read even in a given subfield at a particular conference, and an "old" paper is anything that was published over two years ago. (Who knew Bollywood movies and AI publications would have so much in common?) Maybe there are good reasons why publications should move so much more quickly in AI as opposed to, say, scholastic philosophy, but it's undeniable that it has become a struggle to get others to even read an abstract of your work, and as such we should not be surprised when sensationalization verges on becoming a requirement for your work to get engagement.
So to answer your question--perhaps cynically--“Tiered memory layers to provide extended AI context windows” is not the best title you could have for an AI paper because it has all the rizz of a shipping manifest. If you want to maximize citations, you need to market more.
I also considered whether to blame the field's very young reviewer population for not having the proper disdain for sensationalization that I'd expect from an older researcher who would surely have more restraint than to speak so much more of the sizzle than of the steak, but then I remembered that the paper which introduced the Transformer model was titled "Attention Is All You Need".

### Comment 37898215 by EncomLab depth=2 time=1697455382

I love this response because it's at least honest about the reality of "scientific publishing" today - who cares about the accuracy, verifiability or ability to replicate - you just need to maximize your citations via hype!!"

### Comment 37899524 by althea_tx depth=2 time=1697462500

This isn’t a slight against OP’s paper, but it’s worth noting that arXiv is not peer reviewed.

### Comment 37896486 by pacjam depth=1 time=1697438030

Thanks for your feedback @skrebbel. We called it MemGPT - in reference to teaching LLMs how to manage their own memory hierarchy. The idea and title evolved when we realized we were teaching the LLM to read/write, and this enabled perpetual chatbots, doc QA, etc. Various capabilities by a few simple abstractions, inspired by the original unix paper's 4 key abstractions - read/write/open/close. Further, in the title we say "Towards", indicating a qualified step in that direction.

### Comment 37896558 by skrebbel depth=2 time=1697438992

Perpetual chatbots are a super cool achievement but I fail to see how that resembles an OS, a thing that handles files and lets you run programs, in any way. If MemGPT is as spectacular as you suggest then I think an honest, down to earth title would have gotten you a lot more attention. It seems to me that limited context windows are one of the key roadblocks to wider real-world LLM applicability, beyond demos that do well on Twitter I mean.

### Comment 37897361 by selestify depth=3 time=1697447467

> If MemGPT is as spectacular as you suggest then I think an honest, down to earth title would have gotten you a lot more attention.
The fact that the current title got onto the HN front page suggests otherwise when it comes to incentives for picking submission titles.

### Comment 37896617 by ludwik depth=2 time=1697439634

I think a title like "MemGPT: Operating System inspired memory management for LLMs" would be okay. The current title makes it seem as if you are building an OS based on the LLM technology, which is quite misleading.

### Comment 37896553 by __void depth=2 time=1697438943

still this is not an "operating system" nor does it in any way related to them;
please use the right words when you have to communicate, otherwise you just sound like scammers who want to sell pots with holes by passing them off as colanders

### Comment 37896612 by abdellah123 depth=2 time=1697439598

> we were teaching the LLM to read/write
Very interesting.

### Comment 37896414 by xamde depth=1 time=1697437042

This ist really a succint description: "Sometimes it seems to me that AI people have begun hallucinating as much as the models they’re training."

### Comment 37899008 by fritzo depth=1 time=1697459936

In defense of the authors, I find it helpful to explore analogies between the nascent paradigm of LLM programming and other much older conceptual frames. This paper isn't just tiered memory, but also the analogy between an LLM and a CPU, interrupts, event processing etc.

### Comment 37898225 by amelius depth=1 time=1697455444

This is why we need to get AI (or DL) out of the realm of CS, quickly. Similar to how psychology is a different field than physics even if the former is built on the latter.

### Comment 37897455 by quickthrower2 depth=1 time=1697448450

Attention is all you need. People’s attention that is :-)

### Comment 37896295 by isoprophlex depth=1 time=1697435520

The NFT/web3/shitcoin grifters had their bubble burst, so now they're gravitating towards AI.

### Comment 37898868 by danielbln depth=2 time=1697459131

I hate this take, no matter how often it's repeated. Yes there is hype fever pitch around AI, yes it attracts grifters (as does every hype), but in comparison to crypto, at the very least gen AI provides tractable benefits in a wide array of usecases. What has nft/web3/x-coins ever given us apart from speculative investments (aka gambling)?

### Comment 37899521 by thesuperbigfrog depth=3 time=1697462489

>> What has nft/web3/x-coins ever given us apart from speculative investments (aka gambling)?
Cryptocurrencies modernized the malware industry.
Before cryptocurrencies, ransomware used to require victims to pay using gift cards or other ridiculous means.
After cryptocurrencies, victims could now pay their "captors" directly over the Internet in cryptocurrency.
Before cryptocurrencies, malware entities and actors acted largely independently unless they were part of a state-sponsored group or larger organized crime "business".
After cryptocurrencies, "ransomware as a service" emerged where different groups specialize in particular components and services of ransomware:  tools to establish footholds, tools to take over and encrypt victim systems, services to demand and take payments, and services to wash and launder payments.  Payments between these groups are made in cryptocurrency.

### Comment 37902356 by swalsh depth=3 time=1697474053

The last bull saw the rise of all kinds of new technologies which will enable the use cases people were talking about (Avalanche is my favorite example, but theres some new stuff like SUI coming).  The thing web3 did absolutely right is create a true interchangeable format (ie tokens) the downside is this technology has been developing sooooooo slowly.  Whenever people start to get hope the technology might be ready for use, the gambling use cases rise to the top and dominate.  I think crypto is also dominated by a certain hardline techy.  Or at least it's critics are.  Crypto should be working side by side with traditional finance.  Instead they view it as their enemy.  FTX US is an example of how regulation can be good (the funds on FTX-US were more or less unmolested)  yet most crypto people seem to argue against any regulation at all.  It will be their demise.

### Comment 37896668 by kalium-xyz depth=2 time=1697440292

They already owned the video cards. Might as Well

### Comment 37897797 by HPsquared depth=3 time=1697451753

Nvidia seems to be doing pretty well, at least.

### Comment 37898083 by TeMPOraL depth=4 time=1697454381

We always thought dangerous AIs will be funded by the military, or out of internal R&D budgets of evil multinational megacorps-that-do-everything. Turns out instead it's all been funded by
grifters and scammers
, both large and small. Literally. It's not DARPA or some Umbrella Corporation, but the
advertising companies
that did all the AI R&D, while shitcoiners spent a decade unintentionally funding the hardware AI needs.
Strange reality we live in.

### Comment 37899953 by yowlingcat depth=5 time=1697464549

If you told me a decade ago that this is where we would land, I would tell you to at least make the lie a bit more believable. And yet here we are! Strange times indeed.

### Comment 37903630 by ElevenLathe depth=5 time=1697479114

Agreed, it feels very Stross-ian.

### Comment 37898457 by classified depth=4 time=1697457102

Selling shovels makes you the most money in a gold rush.

### Comment 37898778 by cbm-vic-20 depth=5 time=1697458713

I've never seen the historic mansions of shovel sellers.  I've seen many of railroad owners.

### Comment 37899251 by muzani depth=6 time=1697461271

Well, check out the insane profits (not just revenue) NVIDIA has made this year. That profit margin can fit quite a few mansions as well as the biggest AI companies.
People are joking about the crypto bros funding it, but the leap in profit suggests it's not crypto fueled at all.

### Comment 37902704 by kridsdale3 depth=6 time=1697475277

A railroad is on the continuum that has shovels in it. The job is to get ore from the mine in to a processor.
1. Use you hands
2. Use a pick or shovel in to a bucket and carry it
3. Use a wheelbarrow
4. Use a mine cart
5. Put a steam engine on your minecart

### Comment 37900279 by ultra_nick depth=1 time=1697466302

Are you new to software?
The bugs in programs aren't actual bugs either, windows aren't actual windows, and many would argue that computer science is still more of an art than a science.

### Comment 37895639 by tayo42 depth=0 time=1697426823

This comment section is wild right now btw, no one is responding to the content, just the, i guess, misleading title.
The OS in the title is making a comparison to how page caches work. Relevant data is moved into the context the llm needs to answer chat questions. When it runs out of memory it moves a condensed, searchable version of the content to another data store. Its trying to solve the problem of relatively low max token limits.
I wonder if this makes it easier to run on small devices?

### Comment 37895696 by pacjam depth=1 time=1697427398

Thanks for checking out our work! Yeah, great point, this is even more critical in those scenarios when you have very limited memory. You can play around with different context sizes using the code on GitHub:
https://github.com/cpacker/MemGPT/blob/main/memgpt/constants...

### Comment 37902685 by tayo42 depth=2 time=1697475193

Thats cool, thanks for sharing the code!

### Comment 37895684 by danielmarkbruce depth=0 time=1697427263

This paper could be interesting but the title and analogy are so absurd sounding that most people won't read it.

### Comment 37896988 by mgaunard depth=0 time=1697443877

As a software engineer, the last thing I need from my operating system is to be a LLM.
Thankfully, this paper is not that; the name is just misleading.

### Comment 37895462 by lyapunova depth=0 time=1697424786

I think the problem with stuff like this is that in many cases the authors have an idea like "LLMS + ???? = Operating System !"
which is not that hard of an idea to come up with. Generally in each instance of LLM + ???? = "thing", the first papers that come out to fill the ???? with an answer do that in a rush to get on arxiv and so naturally the work is lackluster (since they have barely had time to think about an actual good solution for the ????).

### Comment 37895737 by pacjam depth=1 time=1697427911

Hey OP, thank you for the post. In this work, we are looking at one particular functionality of an OS - memory management. The project started off motivated by trying to extend context length for a project we were working on. The analogy to OSes came naturally as the project progressed and there was growing similarity to the caching and memory hierarchy relation.

### Comment 37895663 by BasilPH depth=1 time=1697427021

My initial reaction when reading the title was the same. Their abstract does a better job at explaining what they actually do, and where the connection with an OS comes in:
> To enable using context beyond limited context windows, we propose virtual context management, a technique drawing inspiration from hierarchical memory systems in traditional operating systems that provide the appearance of large memory resources through data movement between fast and slow memory.

### Comment 37895585 by SV_BubbleTime depth=1 time=1697426328

Did you think these people just stopped existing when crypto took a dump? Blockchain all the things… LLM all the things!
At least LLMs have a very obvious use from day1… but an OS is not one of them.

### Comment 37901689 by blovescoffee depth=2 time=1697471746

Did you read the paper before commenting?

### Comment 37895692 by lacrimacida depth=2 time=1697427384

You’re probably thinking of a traditional OS. This could be an interesting project though.

### Comment 37894980 by behnamoh depth=0 time=1697419305

People have to stop treating LLMs and transformer models like they're the solution to everything. Never before had I seen so much jump on a hype by academics (I'm an academic too). Honestly it feels like mostly clout seeking and a way to improve citation numbers.

### Comment 37895400 by gmerc depth=1 time=1697423810

Transformers are a primitive we have not fully figured out yet. So it’s perfectly fine to see where this primitive fits.
For example, this week several papers on time series forecasts indicate they may have use there.
For example they seem to do better job on translation than previous approaches.
For example they seem to do a better job at transcription than previous approaches.
Probably will do better on OCR than previous approaches.
Probably has flaws that limits scenarios requiring high precision we may or may not overcome
Possibly will better on autonomous decision making (Does x include  a privacy leak should be investigated?) than previous approaches (keyword scanning).
We are in a technological wave of discovery and experimentation, calls for restraint of curiosity and research betray fears

### Comment 37895487 by sigmoid10 depth=2 time=1697425082

It goes way beyond that. Transformers are the first practical, scalable, general-purpose differentiable (i.e. trainable with gradient descent) algorithm. We haven't come close to seeing the limits of what they can do, because everything so far points to the fact that their only limit is our current hardware. And hardware is improving at a much faster and steadier rate than algorithms in computer science these days.

### Comment 37895669 by sterlind depth=3 time=1697427060

everything? they've solved reinforcement learning? they can handle continuous domains, like robot motion? that's funny, I thought they could only handle sequences of tokens.*
yes, they're exciting, and they are the most general architecture we've found so far, but there are important problems in AI (like anything continuous), that they're really not suited for.
I think there's better architectures out there for many tasks, and I'm a little dismayed that everyone seems to be cargo-culting the GPT architecture rather than taking the lessons for transformers and experimenting with more specialized algorithms.
*btw they don't
need
quantized tokens, there's no reason they can't just work on continuous vectors directly, and they don't have to be causal or limited to one sequence, but "transformer" seems to mean GPT in everyone's mind, and even though the original transformer was an encoder-decoder model we rarely seem to see those these days for some reason.

### Comment 37895693 by famouswaffles depth=4 time=1697427391

>they've solved reinforcement learning?
Transformers can do Reinforcement Learning yes.
https://arxiv.org/abs/2106.01345
https://arxiv.org/abs/2205.14953
>they can handle continuous domains, like robot motion?
Yes they can handle it just fine. Excellently in fact.
https://www.deepmind.com/blog/scaling-up-learning-across-man...
https://tidybot.cs.princeton.edu/
https://general-pattern-machines.github.io/
https://wayve.ai/thinking/lingo-natural-language-autonomous-...
I don't know if anyone is saying they're the best at or have "solved" everything but they can damn near do anything.

### Comment 37895649 by esafak depth=3 time=1697426893

I'm not sure about the last assertion. How would you even compare them? It is easier to deploy newer algorithms (software) than hardware.

### Comment 37895928 by sigmoid10 depth=4 time=1697430340

There's two ways you can solve currently intractable problems: Find better algorithms or improve the hardware. It's actually insanely hard to come up with new algorithms, that is why machine learning and AI were lagging behind most of computer science for decades.

### Comment 37897737 by latexr depth=2 time=1697451108

> calls for restraint of curiosity and research betray fears
That kind of rhetoric is dangerously close to the cryptocurrency shills saying all critics are people who are annoyed because they “missed the boat” and didn’t get rich. It’s the kind of generic comment which can be used to discredit anything the interlocutor wants.

### Comment 37898189 by TeMPOraL depth=3 time=1697455184

"There is more where this came from" reads differently based on how interesting/valuable "this" is. Cryptocurrency wasn't producing anything interesting beyond new flavors of old scams, and renewed appreciation for financial regulation. Transformer models and LLMs in particular seem to be blazing through any problem we throw at them, including previously unsolved problems, and every marginal improvement is
instantly
useful (both in terms of capabilities and in terms of $$$ produced). We hit the motherlode here - and it shows no sign of running out just yet.
That's the difference.
And even when we hit the limit of improvement on those models, when scaling up won't make a qualitative difference, we can expect many years of further breakthroughs in applications, as R&D focuses on less obvious applications and making more efficient use of the capabilities available.

### Comment 37898660 by latexr depth=4 time=1697458134

> "There is more where this came from"
That’s not the part of the comment I had an issue with, which is why it’s not the part I quoted. What I commented on is the end, which implies negative intentions on the part of the original commenter.

### Comment 37898036 by arcticbull depth=3 time=1697453993

Makes sense, there's an awful lot of overlap between the ex-crypto community and the AI community.

### Comment 37898537 by gmerc depth=3 time=1697457468

Research and curiosity a miles away from “get instantly rich” and “solution in search of a problem” we’ve seen in crypto.
Given the context of the original comment this was a response to, you’d have to take things out of context to construct this as a generic comment

### Comment 37898895 by latexr depth=4 time=1697459250

> Research and curiosity a miles away from “get instantly rich” and “solution in search of a problem” we’ve seen in crypto.
And what the original comment boils down to is “let’s not make LLMs and transformers solutions in search of problems, let’s not try to fit them to solve everything”. It seems you might agree.
My issue with the response has nothing to do with specific technologies, but that it painted another view as having an agenda (fear).
That
is the generic defence. You take something you believe and then say those who disagree do so due to
.
By the way, this is not the point but
there are
plenty of “solution in search of a problem” and “get instantly rich” (including full-on scams) cases in the current wave of AI.

### Comment 37895248 by cle depth=1 time=1697422144

I'm struggling to find where these authors are treating LLMs and transformers like they're the solution to everything, or where they are just following hype around? These are long-time AI researchers at Berkeley who've developed a framework for dealing with limited context windows, drawing inspiration from operating systems.

### Comment 37895360 by behnamoh depth=2 time=1697423257

"LLMs as Operating Systems"... —long-time AI researchers at Berkeley

### Comment 37895385 by danenania depth=3 time=1697423646

In the paper, they're talking about managing LLM context windows the way operating systems manage memory and files. They're not saying LLMs should be used as operating systems.

### Comment 37895813 by dstanko depth=4 time=1697429027

they should work on their communication skills.

### Comment 37895986 by another_story depth=5 time=1697431256

This is unhelpful. People should be expected to read past headlines. The paper's abstract takes 30 seconds to read.

### Comment 37896328 by dstanko depth=6 time=1697435963

I'm sorry it's unhelpful, but it is how I feel about the article and click-baity title. downwote all you want.

### Comment 37896498 by xcv123 depth=7 time=1697438168

Always cringeworthy when the average bum coder on HN with zero attention span or intellectual curiosity criticizes papers way out of their intellectual depth without reading further than the title. They are describing a new concept using "operating system" almost as a metaphor. This is a way to describe novel concepts. The article abstract makes the point clear and only takes a few seconds to read.

### Comment 37895070 by Scipio_Afri depth=1 time=1697420153

The branding on this is a bit much, it’s not an operating system. However LLMs are the real deal, some papers claim they are achieving SOTA or significant breakthroughs in various domains. Surely they’re computationally intensive, but if you have read the most of the papers out of Berkeley, Microsoft, Meta, Google/DeepMind/Waymo… I think you’d have an change in opinion.

### Comment 37895189 by TerrifiedMouse depth=2 time=1697421459

> However LLMs are the real deal
Weird thing is it was designed to model language. It’s surprising that it returns sound answers as often as it does. But that’s also kind of the problem, it’s “surprising”, i.e. we don’t really know what happened.
You wouldn’t fly on a jetliner that’s “surprising it flies without disintegrating midair”.

### Comment 37895277 by s17n depth=3 time=1697422509

People were pretty surprised by the Wright flyer.  Confidence is built by experience, not theoretical understanding.

### Comment 37896228 by ravetcofx depth=4 time=1697434414

Science being iterative, they definitely weren't the first to fly, and not even in a heavier than aircraft, what they did acheive was the first time the pilot had 3-axis control, and was the first powered heavier than air manned flight.

### Comment 37895853 by unblough depth=3 time=1697429569

> Weird thing is it was designed to model language. It’s surprising that it returns sound answers as often as it does.
Is this surprising? Can you point to researchers in the field being “surprised” by LLMs returning sound answers?
> “surprising”, i.e. we don’t really know what happened.
This ie reads like a sort of popsci conclusion.
We know exactly what happened. We programmed it to perform these calculations. It’s actually rather straightforward elementary mathematics.
But, what happens is so many interdependent calculations grow the complexity of the problem until we are unable to hold it in it our minds, and to analyze its decisions computationally necessitates similar levels of computation for each decision being made as what was used to compute the weights.
As for its effectiveness, familiarity with the field of computational complexity points to high dimensional polynomial optimization problems being broadly universal solvers.

### Comment 37899841 by TerrifiedMouse depth=4 time=1697463979

> Is this surprising? Can you point to researchers in the field being “surprised” by LLMs returning sound answers?
It's surprising because it wasn't the intent of LLMs. LLMs are just predictive models that guess the most likely next word. Having the results make sense was never a priority. Early version, GPT1/2, all return mostly complete nonsense. It was only with GPT3 when the model got large enough that it started returning results that are convincing and might even make sense often enough.
Even more mind boggling is the fact that randomness is part of its algorithm, i.e. temperature, and that without it the output is kind of meh.

### Comment 37900337 by unblough depth=5 time=1697466577

> It's surprising because it wasn't the intent of LLMs. LLMs are just predictive models that guess the most likely next word. Having the results make sense was never a priority.
If you took the same amount of data for the GPT3+ but scrambled it's tokenization before training THEN I would agree with you that its current behaviour is surprising, but the model was fed data that has large swaths that are literal question and answer constructions. It's over fitting behavior is largely why it's parent company is facing so much legal backlash.
> Even more mind boggling is the fact that randomness is part of its algorithm
The randomness is for token choice rather than any training time tunable so fails to support the "i.e. we don’t really know what happened" sentiment.   We do know, we told it to flip a coin, and it did.
> i.e. temperature, and that without it the output is kind of meh.
Both without it and with it.  You can turn up the temperature and get bad results as well as you can turn it down and get bad results.
If adding a single additional dimension to the polynomial of the solution space turned a nondeterministic problem into a deterministic one, then yes, I would agree with you, that would be surprising.

### Comment 37906536 by TerrifiedMouse depth=6 time=1697489878

> so fails to support the "i.e. we don’t really know what happened" sentiment
It's less that we don't know what's happening on a micro-level but more that it's surprising that it's producing anything coherent at all on a macro-level - especially with a (necessary) element of randomness in the process.
For most part we don't seem particularly knowledgeable about what happens on a macro-level. Hallucinations remain an unsolved problem. AI companies can't even make their "guardrails" bulletproof.

### Comment 37901601 by blovescoffee depth=6 time=1697471494

If you believe LLMs are fully explainable you should write a paper and submit to arxiv.

### Comment 37901837 by unblough depth=7 time=1697472264

I think this is an uncharitable reading of this thread.
I’m arguing against the breathless use of “surprising”.
My gp explains what I think you overlooked in this dismissive response.
> to analyze its decisions computationally necessitates similar levels of computation for each decision being made as what was used to compute the weights.
Explainable but intractable is still far from surprising for me.

### Comment 37907030 by blovescoffee depth=8 time=1697492367

> It's surprising because it wasn't the intent of LLMs. LLMs are just predictive models that guess the most likely next word. Having the results make sense was never a priority.
If you read through what Hinton or any of his famous students have said, it genuinely was and is surprising. Everything from AlexNet to the jump between GPT-2 to GPT-3 was surprising. We can't actually explain that jump in a formal way, just reasonable guesses. If something is unexplainable, it's unpredictable. Prediction without understanding is a vague guess and the results will come as a surprise.

### Comment 37901642 by famouswaffles depth=4 time=1697471609

>Is this surprising? Can you point to researchers in the field being “surprised” by LLMs returning sound answers?
Lol researchers were surprised by the mostly incoherent nonsense pre-transformer RNNs were spouting years go, nevermind the near perfect coherency of later GPT models. To argue otherwise is just plain revisionism.
http://karpathy.github.io/2015/05/21/rnn-effectiveness/

### Comment 37903131 by unblough depth=5 time=1697476988

From your linked post:
> What made this result so shocking at the time was that the common wisdom was that RNNs were supposed to be difficult to train (with more experience I’ve in fact reached the opposite conclusion). Fast forward about a year: I’m training RNNs all the time and I’ve witnessed their power and robustness many times, and yet their magical outputs still find ways of amusing me.
This reads more like humanizing the language of the post then any legitimate surprise from the author.
The rest of the post then goes into great detail showing that “we DO really know what happened” to paraphrase the definition the op provides for  their use of “surprise”.
> Conclusion We’ve learned about RNNs, how they work, why they have become a big deal, we’ve trained an RNN character-level language model on several fun datasets, and we’ve seen where RNNs are going.
I am pushing back on people conflating the innate complexity of a high dimensional polynomial with a misplaced reverence of incomprehensibility.
> In fact, it is known that RNNs are Turing-Complete in the sense that they can to simulate arbitrary programs (with proper weights).
Mathematically proven to be able to do something is about as far from surprise as one can get.

### Comment 37906059 by famouswaffles depth=6 time=1697488046

>This reads more like humanizing the language of the post then any legitimate surprise from the author.
Lol Sure
>I am pushing back on people conflating the innate complexity of a high dimensional polynomial with a misplaced reverence of incomprehensibility.
We don't know what the models learn and what they employ to aid in predictions. That is fact. Going on a grad descent rant is funny but ultimately meaninglessness. It doesn't tell you anything about the meaning of the computations.
There is no misplaced incomprehensibility because the internals and how they meaningfully shape predictions is incomprehensible.
>Mathematically proven to be able to do something is about as far from surprise as one can get.
Magic the gathering is turing complete. I'm sorry but "therotically turing complete" is about as meaningless as it gets. Transformers aren't even turing complete.

### Comment 37895218 by beoberha depth=3 time=1697421780

Unless you’re using an LLM to fly a plane, your analogy is a woefully bad comparison.

### Comment 37895225 by TerrifiedMouse depth=4 time=1697421919

I guess my point is, if we don’t understand it, we don’t know its failure scenarios.

### Comment 37895373 by jackgolding depth=5 time=1697423492

This is the case with all neural nets/black box AI models and a lot are used in various industries.

### Comment 37895396 by tayo42 depth=5 time=1697423772

What things are not understood about transformers?

### Comment 37895525 by aik depth=6 time=1697425664

All the uses

### Comment 37895260 by omarfarooq depth=5 time=1697422269

There's an LLM for that.

### Comment 37900872 by xcv123 depth=3 time=1697468917

> Weird thing is it was designed to model language.
Not exactly. They are designed to perform natural language processing (NLP) tasks. That includes understanding language and answering questions.

### Comment 37895253 by mistermann depth=2 time=1697422202

Depends what "operating system" means.  I'd say things like democracy, marketing/journalism/propaganda, etc are operating systems of some sort, in that they perform orchestration of humans, modify reality, etc.   Lack of memory is a big handicap for LLM's if they want to play in that league.

### Comment 37895502 by hlfshell depth=1 time=1697425324

We have found a new hammer and everything very much looks like a nail.
It's perfectly natural and allows us to figure out what does and doesn't work, even if it means sometimes we have to deal with empty hype projects.

### Comment 37898926 by danielbln depth=2 time=1697459459

This wave of AI hype really brought out the curmudgeons, didn't it? Here we are, with this exciting architecture that is surprisingly applicable to a wide range of problem domains, yet we get "this is like crypto all over again!!1" and "oh everything looks like a nail now, huh?". I mean dang.

### Comment 37895072 by avmich depth=1 time=1697420158

Judge it by its merits.
If the object of hype adds useful novelty, the interest could be justified. If, as it's often the case, it is not quite known - it's a question to figure out.
Granted, intuition is worth something, but it's still not a certainty, so somebody having a different opinion still could see something useful here.

### Comment 37895039 by anon291 depth=1 time=1697419877

I would agree, but on the other hand, Transformer (or attention really) based models seem to be the first time that computers are generating ad hoc human text on a variety of topics, so I do believe the hype is justified. I mean... people have spent entire careers in pursuit of this goal, and it's here... as long as what you want to talk about is less than 4096 / some K tokens.
Given how little progress (relatively) was made until transformers, it seems totally reasonable to pursue att ention models.

### Comment 37901131 by necovek depth=2 time=1697469871

And as long as it is English. How well do they work for other languages with large corpuses?
I know they suck for Serbian, but I wonder what kind of corpus they need to become useful?

### Comment 37901644 by blovescoffee depth=3 time=1697471611

Fwiw I talk to gpt 3.5 in Spanish frequently and there’s no problem that doesn’t exist in the English version.

### Comment 37922850 by necovek depth=4 time=1697584614

Interesting: I do wonder about slightly more complex languages which have declensions and verb "gender" (eg. in Serbian "pevala" means "(a female) sang", whereas "pevao" means that a male did. Or nouns and adjectives can be in 7 declensions: "plavom olovkom" means "with a blue pen", whereas "a blue pen" is just "plava olovka".
ChatGPT always mixes these up, hallucinates a bunch of words (inappropriate prefixes, declensions etc and is very happy to explain the meaning of these imaginary words), and I can imagine smaller, more complex languages like Serbian needing even larger corpuses than English, yet that's exactly the hard part: there is simply less content to go off of.

### Comment 37895043 by infecto depth=1 time=1697419919

I agree they are probably being over-applied but I for one am fascinated and excited for the future and all the possibilities. It’s amazing how much effort is being applied across the board and failures to me just progress other research.

### Comment 37895126 by pylua depth=1 time=1697420749

It deserves to be explored. A lot of research is just applying existing techniques to problems with a few tweaks and documenting the results.
I did not read the paper, but it could be that the authors find it is not effective.

### Comment 37895371 by IOT_Apprentice depth=1 time=1697423473

Sure if the initial blockchain hype  I remember people wanted to build a OS.

### Comment 37895378 by yieldcrv depth=2 time=1697423565

Some of those “OS”es did launch, but theyve been rebranded to SDKs

### Comment 37895424 by nyolfen depth=1 time=1697424133

they are very clearly the most powerful technological innovation i've witnessed in my adult life. we don't even know what they're capable of yet, we're like one year into discovering practical usecases and they are improving at a constant dizzying rate. this is the time for exploration and experimentation.

### Comment 37895136 by keyle depth=1 time=1697420852

I'm a software developer, I live in the concrete world.
To put it in layman's terms, LLMs are to software developers what power tools were for tradesmen.
Sure you can still use your old screw driver, and for some work, it's not worth getting your electric drill out; but it's a game changer.
Sometimes, the hype is justified. I believe at the OS layers, LLM support would make sense. It's full of old mental constructs and "I have to remember how to do this".

### Comment 37895413 by rvz depth=1 time=1697424023

Precisely this. This doesn't solve anything and appears to be absurd techno-solutionism at this point.
Every single problem does not need to be solved using an LLM, which this paper tells us the amount of desperation in this hype cycle.
Those reading this paper and giving it credibility have fallen for this nonsense and are probably gullible enough to believe in this non use-case.

### Comment 37898944 by danielbln depth=2 time=1697459550

> Every single problem does not need to be solved using an LLM
How do you know if a problem is suitable for transformers/LLMs unless you try? We have this great generalized architecture, I would hope people throw everything at it and see what sticks, because what's the downside? Less focus on bespoke predictive models? Oh no.

### Comment 37896774 by Philpax depth=2 time=1697441620

Did you read the paper? What exactly do you think it does?

### Comment 37895376 by greatpostman depth=1 time=1697423540

LLMs are a step function change in computers
