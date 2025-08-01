from agents.Ideation_agent import Ideation_Agent
from agents.scripting_agent import ScriptingAgent
from agents.post_analyzer_agent import PostAnalyzerAgent

def run_pipeline_v1(topic: str):
    print("\n[Step 1] Ideation")
    idea_agent = Ideation_Agent("IdeationAgent", "Generate creative content ideas")
    ideas = idea_agent.run(topic)

    print("\n[Step 2] Script Generation")
    script_agent = ScriptingAgent(name = "ScriptAgent", prompt =  "Generate a script for one idea")
    script = script_agent.run(ideas[0]["description"])

    print("\n[Step 3] Post Analysis")
    analyzer = PostAnalyzerAgent("PostAnalyzerAgent", "Analyze post engagement or quality")
    analysis = analyzer.run(script)

    return {
        "idea": ideas[0],
        "script": script,
        "analysis": analysis
    }
