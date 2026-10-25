---
title: "A 20-minute CNN fine-tune beat GPT-6 Astra at skin cancer"
date: 2026-10-26
summary: "On October 25 the dermatologist Magnus Lynch published a test on his blog. He showed 200 biopsy-proven skin lesions to GPT-6 Astra and Claude Fable 5.1, then…"
---

## A 2015 CNN retrained in twenty minutes beat GPT-6 Astra and Claude Fable 5.1

On October 25 the dermatologist Magnus Lynch published a test on his blog. He showed 200 biopsy-proven skin lesions to GPT-6 Astra and Claude Fable 5.1, then showed the same 200 lesions to a CNN built from Google's 2015 Inception v3. The CNN named the right diagnosis first for 125 of the 200 (62%). The two LLMs managed 84 and 85 (42% each). Allowing a second choice, the CNN reached 173 and the LLMs 134 and 138. [Lynch Lab](https://lynchlab.net/llm-skin-cancer)

The lesions came at random from MILK10k, a public dataset, and every one of them carried a histopathology result. Half should not be discharged: 30 melanomas, 25 basal cell carcinomas, 25 squamous cell carcinomas and 20 actinic keratoses. The other half were safe to discharge: 50 benign naevi and 50 seborrhoeic keratoses. The CNN is Inception v3, pretrained on everyday photographs and fine-tuned on 68,011 dermoscopic and clinical images from the ISIC Archive on a single H100. The 200 test lesions were removed from its training data. Fine-tuning took about twenty minutes, and the model runs in a phone browser through WebGPU without uploading anything. [Try the CNN](https://lynchlab.net/skin-ai-inception)

Neither LLM's errors were scattered. GPT-6 Astra called 75 lesions basal cell carcinoma when 25 of them were, and 14 of those 75 were melanomas. Claude Fable 5.1 called 53 lesions actinic keratosis when 20 were. The CNN erred the other way: of the 17 melanomas it missed, it called eight benign naevi and six seborrhoeic keratoses.

This is one dermatologist testing 200 lesions, with both LLMs run zero-shot at default settings. It is not a clinical result.

## If the task is narrow and the labels exist, test a small model first

The usual build order starts with the best available LLM. This test shows where that order is weakest: a fixed answer set, a few hundred labelled examples, and accuracy as the product. Here a classifier trained in twenty minutes beat two frontier models, costs nothing per call, and runs inside the browser, so images never leave the device. The same shape shows up beyond dermatology: spotting defects in photos, or sorting incoming tickets into fixed categories.

The number worth taking from the test is not 62 against 42, it is the error table. Each LLM had a favourite answer: basal cell carcinoma 75 times out of 200 when 25 lesions were, actinic keratosis 53 times when 20 were. Errors that collapse onto one class are the kind you can fix with more labels, and you only see them if you bring your own test set. Two hundred labelled items of your own will tell you more about a model than any launch table.

One small test settles nothing about models in general. With 200 lesions, a single author and one prompt per case, the LLMs lost under these conditions rather than everywhere. A narrow classifier and a conversational model are good at different places, and that boundary is something you measure on your own data.

## The rest of today's news

- **Five denial-of-service flaws landed in vLLM below 0.31.0**: one unauthenticated request can stall the inference engine for every user, and one flaw lets an API caller make the server connect to an attacker's host. CVSS reaches 8.8. [GitHub](https://github.com/vllm-project/vllm/security/advisories)
- **OpenAI is offering discounts of up to 90% to win Anthropic customers**: The Decoder summarised The Information's report. Rippling's coding traffic moved from 57% Anthropic in May to 18%, and DataCamp says its costs fell 80-90%. [The Decoder](https://the-decoder.com/openai-offers-discounts-up-to-90-percent-to-poach-anthropics-biggest-customers/)
- **Kimi K3.1 Pro faces allegations of undisclosed paid promotion**: screenshots circulated that appear to instruct creators to drop paid-partnership labels. Their authenticity is unconfirmed, and Moonshot has not responded. [VentureBeat](https://venturebeat.com/technology/moonshots-kimi-k3-1-pro-flirts-with-open-weights-leadership-amid-paid-influencer-scandal-allegations)
- **SpaceX raised $40 billion for GPUs**: Musk called it callable debt for chips arriving in the first half of next year. He said the 200-plus neoclouds locked out of credit are heading for consolidation. [Reuters](https://www.reuters.com/business/media-telecom/musk-says-spacex-raised-40-billion-debt-gpus-2026-10-25/)