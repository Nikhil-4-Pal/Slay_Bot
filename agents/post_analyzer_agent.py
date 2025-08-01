from agents.base_agent import BaseAgent

class PostAnalyzerAgent(BaseAgent):
    def __init__(self, name="PostAnalyzerAgent" , prompt : str = ""):
        self.prompt = """You're an expert short-form content strategist. 
Analyze the following content:

"{content}"

Break down:
1. Hook strength (0-10) and why
2. relatability level
3. Content structure and pacing
4. Audience appeal
5. Improvements (hook, delivery, CTA, visuals, sound)

Be highly critical like very critical but constructive. Format response with short paragraphs and numbered points.
"""
        super().__init__(name=name, prompt=prompt)

    def format_prompt(self, content):
        return self.prompt.format(content=content)