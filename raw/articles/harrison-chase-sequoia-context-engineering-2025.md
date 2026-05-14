---
source_url: https://sequoiacap.com/podcast/context-engineering-our-way-to-long-horizon-agents-langchains-harrison-chase/
fetched_url: https://sequoiacap.com/podcast/context-engineering-our-way-to-long-horizon-agents-langchains-harrison-chase/
source_type: interview
author: Harrison Chase / Sequoia
source_date: 2025
ingested: 2026-05-14
sha256: 80f9d1f1fcea462788021d14444ca962ce35acc91e67baf4858d2287dc3464de
raw_preservation: full_html_article_text_candidate
extraction_method: readability_lxml_html2text
html_bytes: 115558
parsed_chars: 46579
---

# LangChain’s Harrison Chase: Context Engineering Long-Horizon Agents

## Source Metadata

- Source URL: https://sequoiacap.com/podcast/context-engineering-our-way-to-long-horizon-agents-langchains-harrison-chase/
- Fetched URL: https://sequoiacap.com/podcast/context-engineering-our-way-to-long-horizon-agents-langchains-harrison-chase/
- Source type: interview
- Author: Harrison Chase / Sequoia
- Source date: 2025
- Ingested: 2026-05-14
- Reliability: medium-high
- Raw preservation status: full_html_article_text_candidate
- Extraction method: readability_lxml_html2text

## Parsed Source Text

#### Introduction

**_Harrison Chase:_**_People use traces from the start to just tell what’s going on under the hood. And it’s way more impactful in agents than in single LLM applications. Because in single LLM applications you get some bad response from the LLM, you know exactly what your prompt is, you know exactly what the context that goes in is because that’s determined by code, and then you get something out. In agents, they’re running and repeating. And so you don’t actually know what the context at step 14 will be, because there’s 13 steps before that that could pull arbitrary things in. So, like, what exactly is—everything’s context engineering. Context engineering is such a good term. I wish I came up with that term. Like, it actually really describes everything we’ve done at LangChain without knowing that that term existed. But, like, traces just like tell you what’s in your context. And that’s so important._

**Sonya Huang:** Welcome to Training Data. Harrison, you were our very first guest on Training Data. And the AI space has moved so quickly in the 18 months or so since we originally interviewed you, and so I’m delighted to get you on the show today. Topics of the moment, I think there’s nobody better than you to talk about some of these topics. We’re going to talk first about long-horizon agents and agent harnesses. Pat and I had this blog post on this yesterday. I know this is something that you are deeply fluent in.

And then we’re going to talk about what’s the difference between building long-horizon agents versus building software, and the role that you see LangChain playing in that ecosystem. And then finally, I just want to chat with you about the future. I think you singlehandedly kind of saw the agent opportunity, I think, before anybody—you know, we were back in the GPT-3 days, and I think you see the future for what’s happening with agents. And so I’m just excited to chat with you open-endedly about the future as well.

**Harrison Chase:** I am really excited as well. Thank you guys for having me back. It’s quite an honor. I’ll tell my mom again that I’m back on the podcast.

#### Main conversation

**Harrison Chase:** I am really excited as well. Thank you guys for having me back. It’s quite an honor. I’ll tell my mom again that I’m back on the podcast.

**Sonya Huang:** [laughs] Wonderful. Okay, let’s start with long-horizon agents.

**Harrison Chase:** Yes, that was a great term. You guys wrote a great article.

**Pat Grady:** Sonya’s good at naming things.

**Sonya Huang:** We’re not going to get into the backstory there. What do you think? What do you agree with? What do you disagree with?

**Harrison Chase:** I mean, I agree that they’re starting to finally work. I think, like, the idea of running an LLM in a loop and just having it go was always the idea of agents from the start—AutoGPT was basically this. Then this is why it took off and captured so many people’s imagination, because it was just an LLM running in a loop, completely deciding what to do. The issue is the models weren’t really good enough, and the scaffolding and harnesses around them weren’t really good enough.

And I think the models got better. We learned more about what makes a good harness over the past few years, and now they start to really, really work. And you see this in coding first. And I think that’s the domain where they’re taking off the most, and that’s spreading to other domains. But you can give a task to an agent, and you still need to communicate to it what you want it to do and it needs to have the right tools and all of that, but it can actually operate for longer and longer periods of time. And so the long horizons framing of it, I think, is really, really apt and really, really good.

**Sonya Huang:** Awesome. What are your favorite examples of long-horizon agents? And I guess what shapes do you see them taking?

**Harrison Chase:** So coding is the place where there’s the most. I think that’s the one that I probably use—yeah, that’s the one that I use the most. Adjacent to that, I think, like, really good ones are AI SREs. So Traversal, I think, is a Sequoia company, and they have an AI SRE that operates over longer time horizons.

Research in general—and I’d call AI SREs kind of research. Like, they’re taking an incident and they’re going and digging through logs. Research in general is a really, really good task, because it ends up producing like a first draft of something. And the issue with agents is they aren’t reliable to nine nines of reliability, but they can do a ton of work, and more and more work over longer time horizons. So if you can find these framings where they run for a long period of time but produce, like, a first draft of something, those to me are the killer applications of long-horizon agents right now.

So coding is an example of that. Like, coding you usually put up a PR. You don’t directly push to prod unless you’re vibe coding, which is also starting to get better and better. AI SREs usually surface it to a human who comes in and then reviews it. Report generation, you don’t send it out to all of your followers right away. You look at it, you edit it, it creates a first draft of something. So we see this in finance a bunch. This is a huge research opportunity.

Customer support, we see a lot of things pivoting from kind of like—the initial customer support was first line response, like someone messages, you just respond really quickly. And there’s still that, and that’s going great. But now there’s examples—Klarna’s a great example of this—where it’s like humans and AI working together. When the first line fails, you escalate to a human. You don’t just have the human handle it, you have this long-horizon agent run in the background, produce a report of everything that happened, and then hand it off to the agent there—to the human agent there. “Agent” starts to get confusing in customer support.

**Pat Grady:** Yeah. [laughs]

**Harrison Chase:** So I think the killer use case of all of these is places where you have this first draft type of concept.

**Sonya Huang:** And then how much of the why now? Do you think is the models themselves are just so good versus people are doing really smart things on the harness side? And maybe even before we get to that, can you say a word for our listeners on how you frame the harness versus the model in terms of the actual composition of an agent?

**Harrison Chase:** Yeah. And I’ll maybe bring in, like, framework as well, because I think early on, I mean, that’s how we described LangChain. That’s what a langchain is. It’s an agent framework. And now we have deep agents, which I’d call an agent harness. And we get asked about what’s the difference?

So a model is obviously the LLMs, tokens, messages in, messages out. The framework would be abstractions around that, so making it easy to switch between models, adding abstractions for other things like tools and vector stores, memory and things like that, but pretty unopinionated about what actually goes in there. The value is more in abstractions, which can be good, can be bad.

Harnesses are more like batteries included. So when we talk about deep agents, we’re talking about we actually give it a planning tool by default. So it has a tool that comes built into the harness. That’s pretty opinionated that this is the right way to do things.

We do compaction. So you have these long-horizon agents, they’re running for long periods of time. Context windows are larger, but they’re still not infinite. And so at some point you need to compact that. How do you do that? There’s a lot of research going on there right now.

One of the other sets of tools that we and a lot of people are giving to these agents are tools for interacting with the file system, whether directly or via Bash. And it’s kind of tough to separate from the models, because the models are being trained on a lot of this data as well. And so there’s this kind of evolution between, like, I don’t know if we could have known that these file system-based harnesses are the best thing. If we go back two years ago, I don’t think we could have known that, because models weren’t really being trained on that as much as they are now. And so they’re kind of evolving together.

So I think it’s a combination of things. The models absolutely are getting better. Reasoning models are helping a lot. But it’s also the fact that we’re figuring out all these [inaudible] around compaction and planning and these file system tools being really useful. And so I do think it’s a combination of both.

**Sonya Huang:** I remember in that very first episode we did together, you described laying graph, I think, as almost the cognitive framework of the agent. Is that the right way to think about what the harness is?

**Harrison Chase:** Yeah, I think that’s right. Yeah. So we build deep agents on top of LangGraph. It’s one particular kind of, like, LangGraph instance. It’s very opinionated. It’s more general purpose. And so I think early on we talked about general purpose architectures and more specific architectures, and what we’ve seen is that a lot of the specificity for tasks previously that might have been in LangGraph because you need to put more structure on the models, now that specificity is moving into the tools and the instructions. So there’s still the same level of complexity. It’s just in natural language. And so prompting and editing those prompts and maybe automatically updating those is becoming a part, but the harness is remaining a little bit more fixed.

**Sonya Huang:** What’s the hardest thing to get right on the harness side? And do you think individual companies can actually excel at the harness engineering side of things? Who do you admire there?

**Harrison Chase:** I think a lot of the companies that are doing the best harness engineering are coding companies, honestly. I think that’s the place where it’s taken off a bunch. I mean, you look at Claude Code, I would argue a big reason for the popularity of Claude Code is the harness itself.

**Pat Grady:** Does that, by the way, imply that harnesses are better built by foundation model companies than by third-party startups?

**Harrison Chase:** I don’t know. So the next company I was going to mention is Factory, which is another coding company. And I think you look at the harness they’ve done there. Amp is another coding company that has a really good harness.

I think there’s pros and cons. There definitely is some aspect of the harness being tied to a model, and maybe not a specific model, but a family of models. So all Claude models, like, Anthropic fine tunes on some specific tools. OpenAI fine tunes on different ones. So I think probably when we were doing this last time, we maybe talked about how prompts need to be different for one model versus another. Harnesses also need to be slightly different for one family of things versus the other. But there are similarities: all of them use the file system in some sense.

So I think this is—I actually don’t know the answer to that. It’s a really interesting thing. We see that a lot of the coding—everyone who’s building a coding company is basically building their own harness right now.

**Pat Grady:** Yeah.

**Harrison Chase:** And there’s all these leaderboards, and you can see—it’s actually kind of interesting. If you go to Terminal-Bench 2.0, which I think is probably one of the more popular coding benchmarks right now, you can actually see they have the agent harness and then the model. And so you can see the variation in performance. And Claude Code is not at the top of that. So there’s differences, but I think it doesn’t necessarily mean that the model labs are better at it. It just means that you have to understand how the models work, and people who look at what makes a harness tick around the model can get some performance gains there.

**Pat Grady:** Yeah.

**Sonya Huang:** What do you think goes into making the harness tick? What do you think the guys at the top of the leaderboard are doing exceptionally well?

**Harrison Chase:** I think part of it is definitely understanding what tools the models trained on. So I think OpenAI trains really heavily on Bash. I think Anthropic has some explicit kind of file editing tools. And so I think leaning into that is part of it.

Compaction is becoming more and more of a thing. So especially as you start doing longer horizon tasks, like, you start to fill up the context window. And so what do you do there is a really big question, and there’s a bunch of strategies for kind of like approaching that. I’d argue that’s part of a harness.

I mean, so all of these harnesses also, this is where, like, skills and MCPs and subagents start to come into play as well. And you can use those in different ways. And I don’t know how—I don’t think a ton of skills or subagents are trained into the models yet. Like, those are still pretty new.

**Pat Grady:** Yeah.

**Harrison Chase:** And so one of the things that we see in our harness is, like, when you have a subagent, the main model needs to communicate with it well. It needs to give it all the appropriate information. It needs to let the subagent know that it needs to give it its final response out. So we would see some failure modes where the subagent—because basically what happens is you kick off the subagent and then only the final response is passed back to the main agent.

And so we’d see some failure modes where the subagent would do a bunch of work, and then it would be basically like, “Look at my work above.” And then, you know, pass that back to the main agent and it can’t see it and it’s like, what are you talking about? And so that type of prompting to get these pieces to work together is a big part of it. So, like, skills, subagents, MCP, there are prompts in all of these harnesses that make them work well or don’t make them work well. And they’re hundreds of lines long if you look at some of the ones that are out there.

**Pat Grady:** Can I ask you a question on how this has evolved? Since you’ve always been really kind of on the bleeding edge of what are people doing around the models to make them work in the real world, right? If we think about in our simplistic view on, like, what the big inflection points over the last five years have been, it feels like there was a big inflection point around pre-training when ChatGPT came out. It feels like there was a big inflection point around reasoning when o1 came out. It feels like just recently there’s been a third big inflection point around these long-horizon agents with Claude Code and Opus 4.5.

In your world, the world of all the stuff around the models that makes them work in the real world, would you have a different set of inflection points? Like, what have the major changes been? I remember we talked about cognitive architectures a couple years ago, and now we’re talking about frameworks and agent harnesses. What are the major leaps in sort of the design around the model? What have they been?

**Harrison Chase:** So I think there’s maybe like three eras I would say. I’d say early on—and this is when LangChain was just started—like, these were still the raw text in, text out, not even chat-based models. And so they didn’t have any of the tool calling, they didn’t have any content blocks, any reasoning at all. They were really just really, really basic. And so the things that people were doing were mostly like single prompts or chains, and it wasn’t even possible to do anything that complicated.

Then a lot of the model labs started training in a lot of the tool calling into the models, and they got really good at—or they tried to make them good at thinking and planning. And they still weren’t good yet. They sort of weren’t good as they are today, but they were good enough to decide what to do. And this is where the custom cognitive architectures would come more into play, because you’d ask it explicitly, like, “What do I do here?” But it was a very point in time. And then you go down this branch, and then “What do I do here?” And maybe there’s a loop, and there started to be some loops, but it’s still a little bit more scaffolding around it.

And then there was an inflection point, and I don’t know where exactly that was. I would say I think we noticed it probably in June, July of this year, where we saw Claude Code taking off, Deep Research taking off, Manus taking off. And these all use the same architecture under the hood of just the LLM running in the loop. But, like, cleverly—like, a lot of hardness is context engineering. Like, everything around [inaudible], context engineering, subagents, context, skills, context engineering. So we basically saw them using the same core algorithm, but making just, like, improvements on context engineering. And we’re like, “Oh, that’s interesting. That’s pretty different than before.” And so that’s when we started working on deep agents.

I think for a lot of people in the coding community, I think probably Opus 4.5 was when they started to really feel this. It might have also just coincided with winter break when everyone went home and started using Claude Code and realized how good it was.

**Pat Grady:** Yeah. [laughs]

**Harrison Chase:** But I think around November, December, like, I think there has been this, at least I sense a pretty big vibe shift. And people just like, yeah, you throw hard problems at these things and you get long-horizon agents. And so I don’t know whether it was early 2025 or late 2025, but at some point the models got good enough, and that’s when we moved from scaffolds to harnesses.

**Pat Grady:** And what’s next on this arc?

**Harrison Chase:** I wish I could tell you. I mean, I do think that, like, this algorithm of just running the LLM in a loop and letting it orchestrate its own—letting it really choose what to pull into context and doing stuff there, that is so simple and so general purpose. Like, I mean, that was the core idea of agents all along. And we’re finally there.

**Pat Grady:** Yeah.

**Harrison Chase:** If you look at some of the manual scaffolding, like, maybe some of that goes away. So, like, compaction is still very manual, like, the harness author decides what to do with it. Anthropic has some interesting things where they let the model decide, like, when to compact things. We don’t really see a ton of people using that. Maybe that’ll be a part that’s next.

Part of what we’re really interested in is memory as well. If you think about memory in the context of this, that’s also context engineering, right? It’s context engineering over longer time horizons, and it’s a slightly different set of contexts, but it’s still giving that to the LLM. And I think the core algorithm is pretty simple. It’s run the LLM in a loop, and we’re finally there and it kind of works. And so I think there’ll be a bunch of context engineering tricks around it.

And maybe some of that is giving the context engineering actually to the LLM, like the Anthropic thing. Maybe some of that is just pulling in new types of context. The models will probably get better—I mean, they’ll probably get better and better at these types of longer horizon tasks. That’ll be great as well.

One of the big questions on my mind is so a lot of these harnesses that we see are very coding specific. And that’s where we first started to really see these long horizon agents take off. And even for non-coding tasks, I think you can make an argument that writing code is really useful and can be general purpose.

**Pat Grady:** I was going to ask you, are coding agents—is that a subcategory, or are coding agents just agents? Meaning the job of an agent is to figure out how to get a computer to do useful stuff. And code is a pretty good way to get a computer to do useful stuff.

**Harrison Chase:** I don’t know. This is one of the big things. So I very, very strongly believe that right now if you’re building a long-horizon agent, you need to give it access to a file system.

**Pat Grady:** Yeah, okay.

**Harrison Chase:** There’s so many things you can do with a file system in terms of context management. When we talk about compaction, one strategy is to summarize but put all the messages in the file system so that if it needs to look it up, it can.

Another strategy is when you have, like, big tool call results, don’t pass it all to the model. Put it in the file system and let it look it up. Now you can do all of that without a real file system, actually, without letting it write code. So we have a concept of, like, a virtual file system where it’s just backed by [inaudible] or something like that, and it’s more scalable. But there are obviously things you can do with code that you can’t do with a virtual file system. You can’t run code in a virtual file system. So, like, writing scripts is really useful for that.

**Pat Grady:** Yeah.

**Harrison Chase:** And I think a coding agent can be general purpose, but I don’t know if that means that today’s coding agents are, if that makes sense. Because I think a lot of the coding agents today are pretty optimized for coding tasks.

**Pat Grady:** Yeah.

**Harrison Chase:** And so I think it’s possible that a general purpose agent is a coding agent, but I don’t know if, like, the reverse is true, if that kind of like makes sense.

**Pat Grady:** Yeah. Yeah, yeah.

**Sonya Huang:** We’re thinking about that a lot as well. Are all agents coding agents?

**Harrison Chase:** Yeah, that’s one of the biggest things that we’re thinking about right now.

**Sonya Huang:** Yeah. Maybe can we transition into talking about what goes into building a long-horizon agent versus building software? Can you maybe describe the software development stack for [inaudible] code development, and what’s different now? And I thought you had a really good X article on this. Maybe just summarize the punchline.

**Harrison Chase:** I think about this a bunch, because we like to say that build—and I think a lot of people would agree that, like, building agents is different than building software. But, like, what exactly is different? Because I think it’s easy and lazy to say that it’s different, but what actually is different? These might sound obvious, but hopefully that’s good and they’re not controversial but, like, when you’re building software, all of the logic is in the code, in the software, and you can see it there. When you’re building an agent, the logic for how your application works is not all in the code. A large part of it comes from the model. And so what this means is that you can’t just look at the code and tell exactly what the agent would do in a specific scenario. You actually have to run it.

And so what does that mean? And I think that’s the biggest difference, by the way. We’re introducing these non-deterministic systems into it, and it’s a black box and it lives outside. And I think all that’s true. That’s the biggest difference.

So what exactly does that mean? I think one thing that that means is that in order to tell what the application is actually doing, you can’t look at the code, you have to look at actually what it does in real life. And so I think one of the things that we do that is most popular is LangSmith. One of the core parts of that is tracing. Why are traces so popular? Because they tell you exactly what goes on inside your agent at every step.

**Pat Grady:** Yeah.

**Harrison Chase:** And it’s different than software traces, where in software you kind of have your system over here, and it emits a bunch of stuff, and you look at it when maybe there’s some errors, but you don’t need everything. And you usually only turn that on when you put it in production, because if it’s local, you just put a breakpoint or something like that.

In agents, people use traces from the start to just tell what’s going on under the hood. And it’s way more impactful in agents than in single LLM applications, because in single LLM applications you get some bad response from the LLM, you know exactly what your prompt is, you know exactly what the context that goes in is, because that’s determined by code, and then you get something out.

In agents, they’re running and repeating, and so you don’t actually know what the context at step 14 will be, because there’s 13 steps before that that could pull arbitrary things in. So what exactly is—everything’s context engineering. Context engineering is such a good term. I wish I came up with that term. Like, it actually really describes everything we’ve done at LangChain without knowing that that term existed. But traces just tell you what’s in your context. And that’s so important.

And so what does that mean? That means that the source of truth for software is in code, and for agents it’s a combination now of code, and traces are where you can see the source of truth. It’s technically in all those millions, billions of parameters, but you can’t really do anything with that, so now that means that traces become a place where you start to think about testing, because now you can test some parts still of the harness and you can do some unit testing offline, but in order to get what the test cases are, you probably want to use the traces to construct that. And you probably want to be testing online. That’s probably more important in agents than it is in software is online testing. Because behavior doesn’t emerge until it’s actually being used with real world inputs.

We see traces becoming a point of collaboration for teams, because if something goes wrong, it’s not, “Oh, let’s go look at the code in GitHub,” it’s, “Let’s go look at the trace.” We see this in our open source as well. When people are being like, “Hey, Deep Agents went off the rails here. What happened?” Our response is “Send us a LangSmith trace. We can’t really help you debug if it’s not that.” Previously it would be like, “Show me the code,” right? So there’s a transition there.

And then I think the other thing that—and so that was the blog post that I wrote next, which got a lot of good feedback on it, and still kind of figuring out how to, like, phrase it. But I think that’s a big part of it.

The other thing which I’m still trying to think through as well, is I think building agents is more iterative. And we used to say that, and I would kind of roll my eyes because building software is iterative as well, right? You ship it, you get feedback, and it’s this constant iteration, that’s like what it is.

I think the difference is that in software you’re kind of like iterating based on what you want the software to do. Like, you have some idea, you ship it, you get feedback. Oh, maybe this button is confusing. Maybe users actually want to do X instead of Y. But you know what the software does before you ship it. With agents, you don’t know what the agent does before you ship it. You have an idea, but you don’t really know what it does before you ship it. And so I think there’s way more iteration involved in order to get it, like, accurate, get it right and passing conceptual unit tests, basically.

And building upon that, this is actually why I think memory is really important as well, because memory is learning from those interactions. And so now you have a process that’s way more iterative, and so now you have to—like, it’s way harder to build as a developer, because I have to change the system prompt way more than I would have to change code in order to get it to just perform correctly.

**Pat Grady:** Yeah.

**Harrison Chase:** So that’s where memory comes in, because if there’s a way where the system can kind of learn by itself, that cuts down the iteration that you have to do as a developer and makes it easier to build these types of agents. So that’s another kind of angle that—I absolutely think agents are different than building software. I think it’s also a little cliché to say that, and so I’ve tried to think about what exactly is different. And those are the two things that I’ve kind of come up with.

**Pat Grady:** And I’m curious on that, too. One of the questions—this is a big public market debate right now is are the existing software companies going to make it? And if you analogize to when on-prem software went to cloud, very few actually did make it because it turned out that building cloud software was actually quite different than building on-prem software.

And since you’re in the middle of kind of how people are building with AI, what’s your take on not necessarily the public market question, but how different is it? Have you seen a lot of people who kind of were good at building software the old way and now they’re good at building software the new way? Or is it more just you either grow up building it the new way or you never get it? Do you think people can make the leap? There’s a lot of young founders out there right now, which makes me think that certainly it seems like the younger people without a lot of preconceived notions on how to build software have the blank slate that has allowed them to pick up on a lot of this stuff.

**Harrison Chase:** I do think we have consistently heard that a lot of the people who are on these agent engineering teams are more junior developers—more junior builders even—who don’t have those preconceived notions. Our applied AI team internally definitely skews on the younger side. I do think—I mean, I think there’s like a person aspect to this. There’s also a company aspect to this. I do think that data is still really, really valuable.

**Pat Grady:** Yeah.

**Harrison Chase:** I think when you think about this harness, basically there’s—like, if harnesses become—by the way, I don’t think that most people will build their own harness in the long run, because it’s actually way harder than building a framework. And so I think they’ll use a harness from us or from someone else.

And so if you think about what goes into that, it’s like the prompt and the instructions, and then the tools that it’s connected to. And I think one thing that—this is more at the company level now but, like, one thing that existing companies have is all the data and all the APIs. If you’ve done a good job at that, then I think it will actually be pretty easy to plug those in and get real value out of things. We were talking to someone in the finance space and they are saying yeah, like, the value of data is just going up and up and up and up. So if you’re a previous software vendor and you have this data that is valuable, like, you should be able to expose it to agents and get a lot of value out of that.

**Pat Grady:** Yeah.

**Harrison Chase:** The other part of it, though, is the instructions on what to do with that data. And that’s probably like more net new in terms of how to use that data. You probably had some ideas about that as a software vendor, but you didn’t kind of like consolidate it. You didn’t have it because that was something that humans would still do. Like, a lot of what agents are doing are what humans would still do. So you’d give them the tools to do it, but you wouldn’t have tried to automate that, or you wouldn’t have successfully automated it before kind of like agents.

And so that part, I think, is newer. And we’re also seeing a lot of demand. Like, I think a lot of the vertical startups—Rogo is a great example of someone who has experience in finance and is bringing that knowledge to agents. And the reason that’s kind of like effective is because a lot of the agents are driven by knowledge. And not like world knowledge, but knowledge on how to do specific patterns. So kind of yeah, I think there’s like—are the people who are building software the right people to build agents? I think we saw a lot of really senior developers adopt agentic coding. And so I think it’s a mindset thing. But yeah, there is maybe a younger skew there, and then for companies it depends on the data.

**Pat Grady:** Yeah.

**Sonya Huang:** Even Pat’s on Claude Code. So yeah, even those guys can get it.

**Pat Grady:** Sonya got me on there.

**Sonya Huang:** [laughs] Okay, so it seems like the trace is a core artifact, you think, in kind of this new world of agent development. And it’s something that LangSmith helps a lot with. What other core artifacts do you think are there? And specifically, I’m wondering about evals.

**Harrison Chase:** Yeah, I think …

**Sonya Huang:** Maybe “artifact” is the wrong word.

**Harrison Chase:** Component?

**Sonya Huang:** Component.

**Harrison Chase:** Yeah. I mean, I think one other thing that is different between building software and building agents is that to evaluate software you could pretty reliably—you could rely on tests and assertions of things programmatically. With agents, a lot of what they’re doing is things that humans would do. So in order to judge them, you need to bring human judgment into that. And that’s another thing that we try to do in LangSmith is how can you bring—you’ve got these traces, how can you bring human judgment into them? And so, like, one obvious way to do that is to bring humans into the equation. And so we see data labeling startups doing really well. We have a concept of annotation cues in LangSmith to bring people in there. And so that, like, actual human judgment is a big part of it.

**Sonya Huang:** And is this is humans annotating the actual trace? So like, oh, the agent did this and this and this, and that was good or bad?

**Harrison Chase:** Yeah. Yeah. And sometimes giving like natural language feedback on it, like, “This is good, this is bad. Should have done this.” Sometimes just correcting it, like actually laying out what the correct steps were. It kind of depends on the use case. And it’s probably different for model companies doing RL than it is for agent companies building agents.

**Sonya Huang:** Yeah.

**Harrison Chase:** But it’s bringing that human judgment to it. But then another thing we see is trying to build proxies for this human judgment. And this is where LLM as a judge type things come in where you can run an LLM or something else that has some semblance of human judgment in it to grade the thing that requires human judgment.

And so one of the things that we think a lot about is how to make building these LLM as judges easy, because a big part of them is making sure that they’re aligned with your human judgment and human preferences. And because if they’re not, you know, then your grader’s just bad. And so we have a concept in LangSmith called “align evals,” where a human goes in, labels some traces, and then that builds an LLM as a judge that kind of like is calibrated against those traces. Because a big part of it is bringing this human judgment, and you just want to make sure that if you’re bringing a proxy of it, it’s well calibrated.

**Sonya Huang:** Interesting. I remember when we first got into business with you, we were emailing about LLM as judge. Is it a viable idea or not? So it seems like it’s come a long way.

**Harrison Chase:** Okay, so there’s a few different aspects of LLM as a judge, right? There’s like the immediate—so what most people use them for in evals is, like, taking this trace and give it a score of, like, 1 to 0 or 0 to 10 or something like that. And yeah, I think that’s viable. And people are doing that. They’re doing it offline, they’re also doing it online, because some of these judgments you don’t need [inaudible] truth for.

But I think the other area where this comes into is—I mean, you kind of see this in the coding agents themselves. Like, the coding agents, they’ll work up until something, then they hit an error and they get an error, and then they have to correct there. And so they’re kind of judging their previous work. And we also see this in memory. Like, a big part of memory is, like, reflecting on traces and then updating something. And so can LLMs reflect on traces that are either, like, their own or their own from a previous session? Yeah, absolutely I think they can. We see this all across evals and just like error correcting and memory, it’s all kind of the same thing.

**Sonya Huang:** I see. And then maybe—okay, so you have all this. You have all the traces.

**Harrison Chase:** Yep.

**Sonya Huang:** You have the evals.

**Harrison Chase:** Yeah.

**Sonya Huang:** I think the natural question that comes to mind for me is, is the eval like a reward signal for reinforcement learning, or is it a feedback mechanism for, you know, a human engineer to improve the harness?

**Harrison Chase:** Or for agent engineers to improve the harness, because no one’s coding manual anymore. They’re all using these—so yeah, one big thing that we’ve seen is, like, we have a LangSmith MCP and we have Langsmith Fetch, which is a CLI, because coding agents are actually great at using CLIs. You give that to an agent, and it can pull down traces and diagnose what went wrong, and then it brings those traces into the code base where it can then fix it. That’s absolutely a pattern that we are seeing, and we really, really, really want to support that pattern.

**Sonya Huang:** Oh, that’s crazy.

**Harrison Chase:** Yeah, I know.

**Sonya Huang:** And it’s good?

**Harrison Chase:** Yeah. Yeah, yeah, yeah, it’s good. Yeah. And so we see—I’m probably more bullish on that than on kind of like reinforcement learning, at least for, like, the agent app kind of like companies right now.

**Sonya Huang:** That seems like real recursive self improvement, though.

**Harrison Chase:** Yeah. I think again, there’s still human in the loop. So, like, back to the point around, like, things are good when you can do something as a first draft. Like, it changes the prompt, and then the human reviews it and it keeps it on the rails.

So one of the things we launched was LangSmith Agent Builder, which is a no code way to build agents. One of the cool things that we have in there is memory. And so right now, the way that memory works is when you interact with an agent—so it’s not in the background yet. It’s not, like, pulling down its traces, but when you interact with the agent, if you say, “Instead of X, you should have done Y,” it will go to its own instructions—which are just files—and it will edit those files so then in the future—and so that’s also kind of like a version of this. One thing we do want to add is like the thing that runs every night, looks at all the traces for the day, updates its own instructions.

**Sonya Huang:** Yeah. It’s the dreaming thing?

**Harrison Chase:** Yeah. Yeah, sleep time compute.

**Sonya Huang:** Sleep time compute, is that what it’s called?

**Harrison Chase:** That’s a term, yeah. I think [inaudible] came up with that. It’s a great term.

**Pat Grady:** That is good.

**Harrison Chase:** Love it.

**Sonya Huang:** Awesome. Okay, let’s talk more about the future. What are you most excited about? It sounds like you’re talking a lot about memory here.

**Harrison Chase:** I like memory a bunch. Yeah. I mean, I think asking the agents to improve themselves is—I mean, I think very, very cool and can be useful in a lot of situations. Not useful in all situations, by the way. So ChatGPT added memory. I don’t actually really use that feature that much, and I don’t think it’s created any more stickiness for me to use the product or anything like that. And I think part of the reason is when I go to ChatGPT, I do—like, everything’s a one-off thing. I don’t really repeat myself that much. I’m asking about software, I’m asking about food, trips, everything. In Agent Builder, you build specific workflows for specific things. So I have an email agent.

**Sonya Huang:** I know. It’s been emailing me for two years.

**Harrison Chase:** [laughs] Well, okay. So I had an email agent outside of Agent Builder, and it had this memory as part of it. We then built Agent Builder, and I wanted to move it into it. And it didn’t have all of my memories and that was a big—even though it had the same starter prompt and the same tools. And that was actually—I still haven’t fully switched over because it kind of sucks now compared to what it was before, like compared to the other one. And if I just interact with it then it will get better and it will stop sucking.

But, like, that’s where memory, I think, can be a real moat. And I absolutely think that we’re at a point right now where LLMs can look at traces and change things about their code. And I think the question then becomes how do you do that in a way that’s safe and acceptable to users? But I think that’s absolutely something that we’ll see more—for specific scenarios, not all of them. Like, I still don’t know if this would be useful in ChatGPT, in this form at least.

**Sonya Huang:** How do you think the UI around working with long-horizon agents will evolve?

**Harrison Chase:** I think there probably needs to be like a sync mode and an async mode. So long-horizon agents running for a long time, probably default would be some sort of like, async way to manage them. Like, if it runs for, like, a day, you’re not just going to sit there and wait for it to finish. You’re probably going to kick off another one and another one and do a bunch of work. And so I think this is where, like, async management of things comes into play.

I think things like Linear and Jira and kanban boards and maybe even email are interesting to look at for inspiration about, like, what it looks to basically manage a lot of these agents. But I think for a lot of these, at some point you’re going to want to switch into synchronous communication with these agents, because they come back with a research report and you want to give it feedback that it wrote something wrong.

And I actually think Chat’s, like, reasonably good at that. The only thing that I’ll maybe say there is that so many of these agents are now modifying other things, like files in a file system, that having some way to view that state is really important. And so you see this in coding, where IDEs are still used when you want to go in and manually kind of change code. And even when I kick off Claude Code, when it finishes, sometimes I pull it up and look at the code that it actually wrote.

And so I think having a way to view that state is interesting. One of the really cool things that Anthropic did with their Claude co-work launch, when you set it up, you choose the directory that it’s working in, and you’re basically saying this is your environment. And obviously, that’s what you do in coding as well, you open your IDE to a particular directory. But I think that’s a nice mental kind of framing is like, this is your workspace. That workspace could be a Google Drive, it could be a Notion page, it could be anything that stores state. And then you and the agent are collaborating on that state. You kick it off, you manage maybe a bunch of these running asynchronously, then you go into sync mode where you chat with it, but you also view the state. And so that’s kind of what I see right now.

**Sonya Huang:** And this is like your agent inbox idea then of, you know, to enable the sync mode, your agent’s going to have to need a way of reaching you.

**Harrison Chase:** Yeah, exactly. And yeah, so the agent inbox, we launched that about a year ago, and had this idea of, like, ambient agents that ran in the background and pinged you. And the first version of that didn’t have a sync mode. And so it would ping you and then you’d give a response, but then you’d kind of just wait for it to ping you again. But oftentimes, like, when I was switching in to email you and respond to you, I would say very small things. And I didn’t want to switch out and wait. Like, you’re really important. So I wanted to, like, be in the sync mode in this conversation with the agent.

And so one of the things we added was now when you open the inbox, you’re brought into chat. And chat is very synchronous, and that was actually a big unlock. So I actually think having just an async mode, I don’t think that really works right now. Maybe in the future if they get so good that you don’t really need to, like, correct them as much, it gets more viable. But at least right now I think we see people switching from async to sync and back and forth.

**Sonya Huang:** What do you think of code sandboxes? Like, is every agent going to have access to a sandbox? Is every agent going to have access to—or a computer? Is every agent going to have access to a browser?

**Harrison Chase:** Really good question. Something we’re thinking a bunch about. I think coding has clearly worked more than browser use so far. So at least in the short term it seems like if any of those are going to be a key part there, it’s going to be this code execution part. File systems, I’m completely file system pilled. I think in some form agents should have access to some file system. Coding, I may be not as pilled, but I’m probably maybe 90 percent there. Yeah, I think it is definitely possible there are—it’s maybe for, like, the longer tail of use cases. So maybe there’s something where if you’re doing something repeated, you need code less. But I think file systems are still useful because that repeated thing could be generating a lot of context, and you need to do context engineering.

But for the long tail of things, coding is great, and there’s really no replacement for that. Browser use, I think the models just aren’t good enough right now from what we’ve seen. You could probably give a coding agent a CLI to do browser use, and there’s probably some approximation there. There’s probably some people doing some—I think I have seen some cool stuff there. And then computer use is like a weird hybrid of the two. So yeah, code sandboxes. I really like code sandboxes.

**Sonya Huang:** Yeah. Cool. Harrison, thank you so much for joining us today. You have consistently seen the future on agents, and it was really cool to have this conversation and talk about how context engineering has evolved to the current point in time with harnesses and long-horizon agents. And so thank you for driving that future, and thank you for always chatting with us about it.

**Harrison Chase:** Thank you for having me on. I look forward to being back on sometime in the future and being completely wrong about everything I said today.

**Pat Grady:** [laughs]

**Harrison Chase:** It’s very hard to predict the future.
