from agents.base_agent import BaseAgent

class MultimodalAgent(BaseAgent):
    def __init__(self , name : str = "" , prompt : str = ""):
        self.name="MultimodalAgent",
        self.prompt="You are a multimodal content agent that generates and enhances social media content using a combination of visuals and text. You describe, caption, or suggest visuals that match the tone and goals."
     
        super().__init__(
            name,
            prompt    )

    def generate_post_with_image(self, concept, persona=None):
        prompt = f"""
You are creating a multimodal social media post idea. The theme is: "{concept}"

Your job:
1. Describe what kind of image should accompany the post (e.g., meme, infographic, selfie).
2. Write a funny, insightful, or viral-worthy caption in the style of: {persona if persona else 'Gen Z relatable tone'}
3. Output should include:
    - Suggested Visual Description
    - Caption

Respond in this format:
- Visual Description:
- Caption:
"""
        return self.run(prompt)

    def analyze_image_and_generate_caption(self, image_description, context=None, persona=None):
        prompt = f"""
You are analyzing a visual for social media posting.

--- Image Description ---
{image_description}

--- Context (optional) ---
{context or 'None'}

Your task is to:
1. Understand the image concept.
2. Generate a humorous or engaging caption that fits the described image.
3. Use persona/tone: {persona if persona else 'funny, casual, Gen-Z'}

Respond in this format:
- Caption:
"""
        return self.run(prompt)
