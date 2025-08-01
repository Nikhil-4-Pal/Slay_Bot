from agents.base_agent import BaseAgent

class CorrectionAgent(BaseAgent):
    def __init__(self , name : str = "" , prompt : str = ""):
        self.name="CorrectionAgent",
        self.prompt="You are a critical and constructive reviewer for AI-generated content. You identify logical inconsistencies, missing elements, vague wording, and areas that could be improved or clarified."
    
        super().__init__(
            name,
            prompt)

    def review_output(self, agent_name, original_output, context=None):
        prompt = f"""
You are reviewing the output of an AI agent named {agent_name}.

Output to Review:
\"\"\"
{original_output}
\"\"\"

{f"Context:\n{context}" if context else ""}

Instructions:
- Identify any factual errors, logical gaps, or unclear phrasing.
- Suggest specific, constructive improvements.
- Do NOT rewrite the entire content unless absolutely necessary.
"""
        return self.run(prompt)
