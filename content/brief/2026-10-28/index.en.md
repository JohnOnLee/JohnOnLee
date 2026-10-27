---
title: "Genie 4 puts a real-time world model before your game engine"
date: 2026-10-28
summary: "Google DeepMind published Genie 4 on October 27. It is a world model that runs in real time. The split from Genie 3 is audio: wind, music, human dialogue, all…"
---

## Genie 4 takes spoken instructions and generates the sound to match

Google DeepMind published Genie 4 on October 27. It is a world model that runs in real time. The split from Genie 3 is audio: wind, music, human dialogue, all generated with the world itself. Type a sentence while a scene plays and the world changes on the spot. [Google](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/introducing-genie-4/) [TechCrunch](https://techcrunch.com/2026/10/27/googles-genie-4-world-model-adds-audio-more-realistic-worlds-and-real-time-steering/)

Genie 4 runs on the Gemini family. Gemini Omni keeps the look and behaviour of objects close to life. Other models in the family supply the reasoning that holds a scene together. Ask for rain and it lands in the scene around you. Between your inputs, Gemini keeps the world moving by itself. Aerodynamics, collisions, natural human motion and speech come out of the same pass.

Gemini also directs. It plans the steps and then checks the frames that come back. In one experiment tied to Gemini Robotics, a Gemini 4 Argon model broke a task into steps and Genie 4 simulated them in real time.

Access is narrow. The model is a research preview for trusted testers. DeepMind plans to open it to Google AI Ultra subscribers in Project Genie and to early access partners on the Gemini API and AI Studio. A scene holds together for up to two minutes, double Genie 3's limit. Run it longer and objects and details drift, and in-world text is still unsolved.

## The check that used to come after the engine now comes first

In DeepMind's tester notes, game developers use Genie 4 to test a visual style or a control idea before writing engine code. The company claims seconds from idea to explorable prototype. For an indie developer this is not a replacement for the game engine: it is the step before engine code, where an idea gets thrown away or kept. A weak direction that dies in the planning stage costs almost nothing, and the same idea built for real costs weeks.

If objects vanish or change shape mid-session, game state built on those frames has no repair path. State and rules stay inside the engine, and the save file stays with them. A world model makes a believable scene on demand. Holding that scene steady is the hard part, and nobody has solved it yet.

Start on the loop today, without the model. Genie 4's pipeline watches the screen, splits a goal into steps, and checks each step before moving on. That loop runs on screenshots and whatever model you already pay for, so pick a few core screens in your product and write down the sentence that means "this state is correct". Then have a model verify against it. If you plan to ship scenes like these, measure what breaks first past the two-minute mark.

## The rest of today's news

- **Stanford Daily: Anthropic trained Claude on Stanford professors' pirated books**: after the $1.5 billion Bartz settlement in May, Tobias Wolff and Chang-rae Lee opted out and are pursuing Cruz v. Anthropic for up to $150,000 per infringed work. [Stanford Daily](https://stanforddaily.com/2026/10/27/professors-books-pirated-to-train-claude/)
- **Apple announced a 14-inch MacBook Pro with M6**: 12-core CPU, 12-core GPU with neural accelerators in every core, up to 25% faster on AI workloads than M5. Pre-orders open October 28, on sale November 6. [Apple](https://www.apple.com/newsroom/2026/10/apple-introduces-the-new-14-inch-macbook-pro-with-m6/)
- **Ghostty shipped 1.4.0**: seven months of work, 172 contributors, 2,889 commits, and the first non-Kitty terminal with a complete Kitty graphics implementation including animation and relative placements. [Ghostty](https://ghostty.org/docs/install/release-notes/1-4-0)
- **Discord will put public server chats in web search**: every Discoverable Server gets a web page from November 16, and public channel messages may appear in search from mid-December. Admins can opt channels out under Server Settings > Web Presence. [Discord](https://discord.com/blog/making-content-from-discoverable-servers-easier-to-discover)