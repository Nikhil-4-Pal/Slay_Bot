from agents.base_agent import BaseAgent

class GoalAgent(BaseAgent):
    def __init__(self, name="GoalAgent", prompt="You manage the primary goals of the project. Ensure that all agent outputs are aligned with the user's overall intent. When asked, evaluate if outputs support or deviate from the goal."):
        self.name = name 
        self.prompt = prompt
        super().__init__(
            name,
            prompt
        )
        self.current_goal = None
        self.subgoals = []

    def set_goal(self, goal: str):
        self.current_goal = goal
        return f"Main goal set: {goal}"

    def add_subgoal(self, subgoal: str):
        self.subgoals.append(subgoal)
        return f"Subgoal added: {subgoal}"

    def get_goals(self):
        return {
            "main_goal": self.current_goal,
            "subgoals": self.subgoals
        }

    def evaluate_alignment(self, agent_output: str):
        prompt = f"""
You are a goal evaluator. The current goal is:
"{self.current_goal}"

Subgoals:
{self.subgoals}

Given the following output:
"{agent_output}"

Evaluate if it aligns with the main goal and subgoals. Be specific.
"""
        return self.run(prompt)
