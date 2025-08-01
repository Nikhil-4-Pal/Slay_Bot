from agents.base_agent import BaseAgent

class SelfCorrectionAgent(BaseAgent):
    def __init__(self , name : str = "" , prompt : str = ""):
        self.name="SelfCorrectionAgent",
        self.prompt="You are a self-correcting AI agent. Given a previous output, you will reflect on its quality, identify flaws or areas of improvement, and produce a corrected or improved version."
    
        super().__init__(
            name,
            prompt )

    def run(self, previous_output: str, context: str = "") -> str:
        prompt = [
            {
                "role": "system",
                "content": self.prompt
            },
            {
                "role": "user",
                "content": (
                    f"Context: {context}\n"
                    f"Previous output: {previous_output}\n\n"
                    "First, reflect on any issues with this output. Then rewrite a better version."
                )
            }
        ]
        response = self.run(prompt)
        return response
