from agents.openrouter_client import call_openrouter

class BaseAgent:
    def __init__(self, name, prompt):
        self.name = name
        self.prompt = prompt

    def run(self, user_input, model="openai/gpt-3.5-turbo"):
        messages = [
            {"role": "system", "content": self.prompt},
            {"role": "user", "content": user_input}
        ]
        return call_openrouter(model, messages)
