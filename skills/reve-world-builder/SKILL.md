---
name: reve-world-builder
description: Build a persistent visual world in Reve — a set of consistent characters, environments, and scenes that hold together across hundreds of images without losing continuity. Use this skill whenever someone needs character consistency across multiple images, wants to build a visual series or story, needs to create a brand mascot or recurring character, or wants to iterate on a visual concept without starting over every time. Triggers include: "keep this character consistent," "build a visual world," "create a series of images with the same character," "make my mascot look the same every time," "build scenes around this person or character," or any request where visual continuity across multiple images matters. Always use this skill before attempting character consistency in any other image generation tool.
---

# Reve World Builder

Most image generation tools treat every prompt as a fresh start. Reve is different. Once you build a world — a character, a setting, a visual style — every image you generate after that inherits the context of that world. You do not have to re-describe your character every time. You do not have to re-establish the environment. You just ask for what you want and Reve already knows where you are.

This is the right tool for building a visual series, a brand mascot, an animated character, a content library for a specific person, or any project where you need more than one image to feel like it belongs to the same world.

---

## What makes Reve different

The key difference is persistent context. Once you feed Reve your reference images and establish a world, the session retains that context. You can ask for "show me her hand" and Reve already knows she is a gold woman in a jungle with a specific face and a specific style — you do not have to say any of that again.

It also generates 10 images at once, which makes iteration fast. You are not waiting for one result, approving or rejecting it, and prompting again. You get a grid, pick what works, and build from there.

The other distinct feature is bounding box editing — the ability to select a specific element in an image and change only that element without regenerating the whole image. Change her hair color. Remove an object. Add something to the background. The rest of the scene stays exactly as it was.

---

## Step 1 — Gather your reference images

Before opening Reve, collect the reference images that define what you are building. These might be:

- Photos of a real person whose likeness you want to recreate as a character
- Stock images or AI-generated images that capture the vibe or style you are going for
- A logo or product you want to place inside scenes
- Screenshots from Dribbble or Pinterest that represent the aesthetic direction

You do not need a lot — three to five strong references is enough to start. Quality matters more than quantity here. Pick images that clearly show what matters most: the face if it is a character, the color palette if it is a brand, the environment if it is a world.

---

## Step 2 — Upload references and establish the world

Upload your reference images into Reve and describe what you want to build. Be specific about the subject, the environment, and the style.

A good world-building prompt looks like this:

> "These reference images show [person/character/style]. Create a world around this subject. The setting is [environment]. The visual style should be [description]. Start by giving me a range of ideas for how this world could look."

Reve will generate a grid of options. Review them. You are not looking for perfection at this stage — you are looking for direction. Pick the one that is closest to what you want and say so. Then ask Reve to build more from that direction.

Once you have a version that feels right, lock it in by saying something like: "This is the world. Every image from here should exist in this world." From that point forward, your prompts can be simple and direct.

---

## Step 3 — Build out the world

With the world established, you can start populating it with the images you actually need. The prompts can be short because the context is already loaded:

- "Show me her walking through the jungle at night."
- "Close-up of her face looking up at something."
- "Wide shot of the entire environment with her in the distance."
- "Show me just her hands holding something."

Each of these will produce images that are consistent with your established world — same character, same environment, same visual style — without you having to re-describe any of it.

Generate in batches of 10. Keep what works, note what does not, and adjust your prompts based on where Reve is drifting from what you want.

---

## Step 4 — Use bounding box editing for precision changes

When an image is close but something specific needs to change, use Reve's bounding box selection tool instead of re-prompting the whole scene.

Click on the element you want to change. Reve will draw a bounding box around it. Then type what you want it to become:

- "Brown hair" — changes only the hair, leaves everything else intact
- "Remove the copyright symbol" — regenerates that area without the element
- "Add a product in her hand" — places something new in the selected area
- "Make the trees darker" — adjusts the selected background element

This is how you get fine-grained control without losing the consistency you built in Steps 1 through 3. It is also how you do brand placements — build your world, then drop a product into specific scenes using bounding box selection.

---

## Step 5 — Export for animation

Once your world is built and you have the stills you need, export the images you want to animate and bring them into Veo 3 via Google Flow. See the `ai-video-production` skill for the full workflow from still image to video.

For controlled animation — where you want specific elements to move without moving the whole scene — use the first frame and last frame technique: create two versions of the image with the element in different positions, set them as the first and last frame in your video tool, and give a simple motion prompt. The video tool interpolates between them. This is how you get things like steam rising from a coffee cup, trees swaying, or a character turning to face the camera.

---

## Use cases

**Brand mascot or character:** Build a character from reference images, establish their world, then generate hundreds of images for social posts, ads, and campaigns — all with the same face, same style, same visual identity.

**Personal brand content engine:** Use photos of a real person as references. Build a world around them. Generate images for their content calendar without scheduling a photoshoot.

**Animated series:** Build your characters and their world first. Then use bounding box editing to move elements and create the illusion of sequence. Export frames into a video tool to animate.

**Logo and brand development:** Start with a reference from Dribbble or a mood board. Iterate through variations using bounding box editing to adjust specific elements. Arrive at a final mark without paying a designer for exploration.

**Product placement:** Build a scene or world, then use bounding box selection to place your product into it. Test different products in the same environment or the same product in different environments.

---

## Notes

- The world-building session is the most valuable asset you create in Reve. Do not rush it. Spend the time in Steps 1 and 2 to get a world you are genuinely happy with before moving into production. Everything downstream depends on it.
- Reve has a free tier that gives you a limited number of generations before requiring payment. Use the free tier to test whether the tool works for your use case before committing.
- The bounding box feature is the single most underused capability in Reve. Most people re-prompt from scratch when something is slightly off. The bounding box approach is almost always faster and produces better results because it does not touch anything that was already working.
- Context does not persist between sessions. If you close Reve and come back, you will need to re-upload your references and re-establish the world. Consider saving your world-building prompt so you can restore context quickly.
- Reve is best for image consistency and world building. For image-to-video, use Veo 3 via Flow. For brand design systems, use Claude Design. Each tool has a specific job — do not try to do everything in one place.
