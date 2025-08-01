from agents.base_agent import BaseAgent

class TrendHunterAgent(BaseAgent):
    def __init__(self, name="TrendHunterAgent" , prompt :str = ""):
        self.prompt = """You are a social media trend analyst for Gen Z content creators.

Your task:
1. Identify currently popular content formats, sounds, or challenges trending on platforms like Instagram Reels, TikTok, and YouTube Shorts.
2. Suggest how these can be adapted to the following content idea or niche:
"{topic}"

Be specific with format (e.g., green screen, voiceover, meme remix), audio suggestions, or stylistic trends. Respond in a friendly and creative tone.
"""
        super().__init__(name=name, prompt=prompt)

    def format_prompt(self, topic):
        return self.prompt.format(topic=topic)