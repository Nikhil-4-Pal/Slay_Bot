from agents.base_agent import BaseAgent

class PassingAgent(BaseAgent):
    def __init__(self , name : str = "" , prompt : str = "") :
        self.name="PassingAgent",
        self.prompt="You are responsible for managing the flow of information between agents in a multi-agent system. Decide which agent should handle the next step based on the content and purpose of the output."
  
        super().__init__(
            name,
            prompt   )
        self.agent_registry = {}

    def register_agent(self, agent_name: str, agent_object):
        self.agent_registry[agent_name] = agent_object

    def route(self, output: str, current_context: str = ""):
        routing_prompt = f"""
You are a router agent. Based on the following output and context, determine which agent in the system should handle it next.

Context:
"{current_context}"

Output:
"{output}"

Registered agents:
{list(self.agent_registry.keys())}

Respond with ONLY the name of the next agent to handle this.
"""
        next_agent_name = self.run(routing_prompt).strip()

        if next_agent_name not in self.agent_registry:
            return f"Error: {next_agent_name} is not a registered agent."

        next_agent = self.agent_registry[next_agent_name]
        response = next_agent.run(output)
        return {
            "next_agent": next_agent_name,
            "response": response
        }
