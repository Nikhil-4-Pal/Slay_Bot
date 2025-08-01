from agents.base_agent import BaseAgent

class EngagementAgent(BaseAgent):
    def __init__(self , name="EngagementAgent" , prompt : str = ""):
        self.prompt="You are an expert in social media engagement. You craft engaging CTAs, questions, comment bait, and interactive post elements to maximize user interaction, especially for Gen Z audiences."
        
        super().__init__(
            name,
            prompt)

    def boost_engagement(self, post_context, tone="casual", platform="Instagram"):
        prompt = f"""
You are helping a content creator increase post engagement on {platform}.

Context: {post_context}
Tone: {tone}

Provide:
1. A compelling CTA
2. An engaging question for the audience
3. A fun comment prompt (e.g., 'Drop your guilty pleasure emoji')
4. One interactive idea (like a poll, challenge, or slider)
"""
        return self.run(prompt)
