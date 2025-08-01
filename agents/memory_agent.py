from agents.base_agent import BaseAgent

class MemoryAgent(BaseAgent):
    def __init__(self, name="MemoryAgent", prompt="You are responsible for storing and retrieving relevant information from past interactions and agent outputs to support decision-making, consistency, and long-term coherence."):
        super().__init__(name=name, prompt=prompt)
        self.memory_store = []


    def store(self, agent_name, output, metadata=None):
        entry = {
            "agent": agent_name,
            "output": output,
            "metadata": metadata or {}
        }
        self.memory_store.append(entry)

    def retrieve(self, query=None, filter_by_agent=None, keywords=None):
        results = self.memory_store
    
        if filter_by_agent:
            results = [entry for entry in results if entry["agent"] == filter_by_agent]
    
        if keywords:
            results = [
                entry for entry in results
                if any(kw.lower() in entry["output"].lower() for kw in keywords)
            ]
    
        if query:
            messages = [
                {"role": "system", "content": self.prompt},
                {"role": "user", "content": f"""
    You are a memory retriever. Given the query:
    \"{query}\"
    
    Select the most relevant entries from the following memory:
    {results}
    
    Respond only with a JSON list of the most relevant entries.
    """}
            ]
            return self.get_completion(messages)
    
        return results

