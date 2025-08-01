from agents.base_agent import BaseAgent

class TrendAgent(BaseAgent):
    def __init__(self, name = "TrendAgent" , prompt = "Find current trends related to topic"):
        prompt_template = """You are a trend scout for content creators. 
Generate 3 trending content ideas in the niche of "{niche}". 

Each idea should include:
- Trend Title
- Why it's trending (context)
- Suggested content angle (humorous, relatable, or satirical)

Tone: Energetic, meme-literate, short-form friendly.
Platform Focus: TikTok, Instagram Reels, YouTube Shorts.
"""
        super().__init__(name = name , prompt =  prompt_template)
    
    def format_prompt(self , niche):
        return self.prompt.format(niche = niche)