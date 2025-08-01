from agents.base_agent import BaseAgent

class ContentRefinerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="ContentRefinerAgent",
            prompt="You are an expert social media editor. Your job is to polish and refine user-generated content to improve clarity, tone, and platform fit."
        )

    def refine(self, raw_text, tone="engaging", platform="Instagram", persona="Gen Z"):
        prompt = f"""
Refine the following post to make it more {tone}, aligned with the platform {platform}, and suitable for a {persona} audience.

--- Original Content ---
{raw_text}

--- Refined Output ---
Please rewrite it using a casual, engaging voice.
"""
        return self.run(prompt)
