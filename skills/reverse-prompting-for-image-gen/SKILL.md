---
name: reverse-prompting-for-image-gen
description: Generate high-quality AI images by reverse engineering existing visuals into detailed text descriptions, then using those descriptions as image generation prompts. Use this skill whenever someone wants to recreate an existing image, generate variations of a visual, combine a subject with a new setting, or build a brand image library without starting from scratch. Triggers include: "make an image like this," "recreate this photo," "put this subject in a different setting," "generate brand imagery," "make a version of this but with X changed," or any request to produce AI-generated visuals from a reference image. Always use this skill before writing image prompts from scratch.
---

# Reverse Prompting for Image Generation

Start from what already exists. Describe it. Use that description as the prompt. This approach produces dramatically better results than writing prompts from scratch because you're working from a real visual reference rather than guessing.

## The core technique

Most people write image prompts forward: they think of what they want and try to describe it. Reverse prompting works backwards: find an image that's close to what you want, have AI describe it in detail, then use that description as the generation prompt.

The output won't be identical — it will be a high-quality interpretation of the original. From there you can swap specific attributes to get exactly what you need.

## Tool stack

- **Image description:** ChatGPT (GPT-4o or GPT-5) — upload the reference image and ask for a detailed description
- **Image generation:** ChatGPT image generation, Midjourney, or any image gen tool that accepts text prompts
- **Fine-tuned generation / compositing:** Reve App for more control over subjects and settings

---

## The workflow

### Step 1 — Find your reference image

Go to iStock, Getty, Pinterest, Dribbble, or anywhere you find a visual that's directionally right. You don't need a perfect match — you need something close enough that its description will point the generator in the right direction.

You can use a watermarked stock image. You're not reproducing it — you're using it as a visual reference to generate something new.

### Step 2 — Get the description

Upload the image to ChatGPT and use this exact prompt:

> "Describe this image in great detail."

ChatGPT will return a dense paragraph covering subject, background, lighting, mood, composition, and color. This is your base prompt.

### Step 3 — Generate the image

Copy the description directly and paste it into your image generation tool. Add two modifiers at the end:

- `Landscape image.` (or Portrait, Square — whatever format you need)
- `Ultra-realistic` (or `cinematic`, `digital art`, `illustration` — depending on the aesthetic)

For Midjourney, append: `--ar 16:9 --v 6.0 --chaos 20 --raw`

The `--chaos 20` parameter introduces controlled variation so you get multiple interpretations rather than one literal render. Adjust up for more variation, down for more precision.

### Step 4 — Swap specific attributes

Once you have a working base prompt, you can change individual attributes by editing specific words in the description. The rest of the scene stays consistent.

Examples:
- Change `white horse` to `brown horse` and the setting, lighting, and composition stay the same
- Change `grassy meadow` to `downtown city street` and the subject stays the same
- Change `golden hour lighting` to `moody overcast` for a different tone

This is more reliable than reprompting from scratch because the full scene context is preserved.

### Step 5 — Combine subject + setting (advanced)

To place a subject into a completely new environment, describe both separately and then synthesize them:

1. Get a detailed description of your subject (the horse, the person, the product)
2. Get a detailed description of your target setting (the western town, the stadium, the office)
3. Feed both descriptions to ChatGPT with this prompt:

> "I'll give you two image descriptions — one for the setting and one for the subject. Your task is to synthesize them into a single, cohesive visual description that reads like a cinematic still or ultra-realistic painting. Abstract both sources so they blend naturally into one moment in time. Keep tone, lighting, and perspective consistent. Ensure the subject interacts authentically with the environment, with physical and atmospheric continuity. End with a short paragraph that captures the overall mood or emotional essence of the combined image — not a summary, but a vivid, unified scene."

Use the synthesized description as your generation prompt. This produces scenes that look like the subject was always in that environment — not a composited cutout.

---

## Building a brand image library

Once you have a base prompt that matches your brand aesthetic, you can lock it and use it as a template. Swap only the variable (landscape type, subject, setting) while keeping all the style parameters fixed.

Example brand prompt template (Gauntlet's):
```
A dramatic monochrome of [enter landscape type], atmospheric depth, moody lighting, 
high contrast, cinematic wide shot, epic scale, ultra-detailed, black and white 
photography / digital art aesthetic --ar 16:9 --v 6.0 --chaos 20 --raw
```

Every image produced from this template is on-brand. You never have to design from scratch.

---

## Notes

- The description step is not optional. Writing prompts from scratch without a reference image produces generic output. The description forces the model to work from a specific visual target.
- Watermarked stock images are fine as references. You're generating something new, not reproducing the original.
- `--chaos 20` is a sweet spot for variation without losing coherence. Go higher if you want more unexpected results, lower if you need consistency across a batch.
- This technique works for any image gen tool that accepts text prompts, not just Midjourney.
