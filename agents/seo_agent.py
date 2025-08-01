from agents.base_agent import BaseAgent

class SEOAgent(BaseAgent):
    def __init__(self , name="SEOAgent" , prompt : str = ""):
        self.prompt="You are an SEO optimization assistant for content creators. You generate SEO-friendly titles, captions, hashtags, and keywords for better visibility across platforms like YouTube, Instagram, TikTok, and blogs."
        super().__init__(
            name,
            prompt
        )

    def optimize(self, content, platform="YouTube", keywords=None, audience="Gen Z", tone="casual"):
        keyword_str = ", ".join(keywords) if keywords else "auto-detect from content"
        prompt = f"""
Optimize the following content for {platform}.

Content: {content}
Target Audience: {audience}
Tone: {tone}
Target Keywords: {keyword_str}

Return:
- SEO Title
- Optimized Caption/Description
- Top 10 Hashtags (if applicable)
- Suggested Tags/Keywords (if applicable)
"""
        return self.run(prompt)
