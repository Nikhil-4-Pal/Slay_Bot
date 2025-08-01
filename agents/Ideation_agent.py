import json
from agents.base_agent import BaseAgent

IDEATION_SYSTEM_PROMPT = """
You are a creative AI assistant for content creators.
Your job is to generate unique, high-engagement content ideas for a specific niche and target audience.
Each idea should be suitable for short-form video (Reels, TikTok, Shorts) or Twitter/X, and include a short description.
Make them catchy, specific, and scroll-stopping — avoid generic advice.
"""

class Ideation_Agent(BaseAgent):
    def __init__(self, name="IdeationAgent", prompt=IDEATION_SYSTEM_PROMPT):
        super().__init__(name=name, prompt=prompt)

    def format_input(self, niche, persona=None, goal=None, platform="Shorts / Reels"):
        prompt = f"Niche: {niche}\n"
        if persona:
            prompt += f"Creator style: {persona}\n"
        if goal:
            prompt += f"Goal: {goal}\n"

        prompt += f"Target platform: {platform}\n"
        prompt += (
            "Generate 5 content ideas. Respond in JSON format like:\n"
            """[
                {"title": "Idea 1", "description": "..." },
                {"title": "Idea 2", "description": "..." },
                ...
            ]"""
        )
        return prompt

    def run(self, niche, persona=None, goal=None, platform="Shorts / Reels"):
        prompt = self.format_input(niche, persona, goal, platform)
        output = super().run(prompt)

        try:
            return json.loads(output)
        except json.JSONDecodeError:
            # fallback: wrap in a single idea if LLM failed to return JSON
            return [{"title": "Generated Idea", "description": output.strip()}]
