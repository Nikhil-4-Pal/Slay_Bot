from agents.base_agent import BaseAgent

class ReflexAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="ReflexAgent",
            prompt="You are a self-reflective agent that critiques and improves AI-generated outputs for quality, consistency, alignment with brand persona, and creativity."
        )

    def review_and_improve(self, agent_name, input_prompt, output_text, persona=None):
        prompt = f"""
You are ReflexAgent. Another agent named '{agent_name}' produced the following output:

--- Agent Input Prompt ---
{input_prompt}

--- Agent Output ---
{output_text}

Your task is to:
1. Identify any logical, creative, or consistency issues.
2. Suggest improvements or rewrite the response if necessary.
3. Ensure it aligns with the intended tone/persona: {persona if persona else 'No specific persona'}

Respond in the following format:
- Reflection:
- Suggested Fix:
- Final Improved Output:
"""
        return self.run(prompt)
