from agents.base_agent import BaseAgent

class WorkflowPlannerAgent(BaseAgent):
    def __init__(self, name="WorkflowPlannerAgent" , prompt :str = ""):
        self.prompt = """You're a content strategist and production manager for Gen Z creators.

Based on the following idea:

"{content}"

Generate a content workflow plan that includes:
1. Pre-production (scripting, tools, props)
2. Production (recording tips, tone, length)
3. Post-production (editing tools, transitions, text overlays)
4. Platform strategy (where and when to post)
5. Optional enhancements (collab, style trends, hashtags)

Keep it short, actionable, and easy to follow also add the people to colab with names , style trends and hashtags to get maximum social media algorithm push. Format as bullet points under each section.
"""
        super().__init__(name=name, prompt=prompt)

    def format_prompt(self, content):
        return self.prompt.format(content=content)