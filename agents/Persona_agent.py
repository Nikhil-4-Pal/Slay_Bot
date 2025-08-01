from agents.base_agent import BaseAgent

class PersonaAgent(BaseAgent):
    def __init__(self, name="PersonaAgent", prompt="You are a persona designer who crafts unique content creator voices."):
        super().__init__(name, prompt)

    def build_prompt(self, niche, audience, tone=None):
        return f"""
You are a persona development assistant for social media creators.

Create a clear and fun persona profile for a content creator in the "{niche}" niche, targeting "{audience}". 
{f'They prefer a "{tone}" tone.' if tone else ''}

Output a structured JSON with these keys:
- persona_name
- tone
- voice
- key_phrases
- emojis
- do
- dont
"""

    def generate_persona(self, niche, audience, tone=None):
        full_prompt = self.build_prompt(niche, audience, tone)
        return self.run(full_prompt)
