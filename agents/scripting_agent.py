from agents.base_agent import BaseAgent

class ScriptingAgent(BaseAgent):
    def __init__(self, name = "ScriptingAgent" , prompt : str = ""):
        self.name = name
        self.prompt = """You are witty and concise Script Writer for short videos.
        Generate a script in three parts: Hook , Main Content , and CTA (Call to Action).
        
        Tone :  Mean , Out of line ,rage bait.
        Target : Instagram Reels and Youtube Shorts.
        
        Title : "{title}"
        Description : "{description}"
        
        Respond in this format :
        Hook : ...
        Main : ...
        CTA : ...
        """
        super().__init__(name = name , prompt = prompt)
    
    def format_prompt(self , title , description):
        return self.prompt.format(title = title , description = description)