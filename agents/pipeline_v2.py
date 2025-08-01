from agents.Ideation_agent import Ideation_Agent
from agents.scripting_agent import ScriptingAgent
from agents.post_analyzer_agent import PostAnalyzerAgent
from agents.workflow_planner_agent import WorkflowPlannerAgent
from agents.trend_agent import TrendAgent
from agents.Persona_agent import PersonaAgent

def run_pipeline_v2(topic: str):
    print("\n[Step 1] Ideation")
    idea_agent = Ideation_Agent("IdeationAgent", "Generate creative content ideas")
    ideas = idea_agent.run(topic)

    print("\n[Step 2] Trend Detection")
    trend_agent = TrendAgent("TrendHunterAgent", "Find current trends related to topic")
    trends = trend_agent.run(topic)

    print("\n[Step 3] Persona Alignment")
    persona_agent = PersonaAgent()
    persona_script = persona_agent.generate_persona(niche=topic, audience="Gen Z", tone="humorous")


    print("\n[Step 4] Script Generation")
    script_agent = ScriptingAgent("ScriptAgent", "Generate a script for the idea")
    script = script_agent.run(persona_script)

    print("\n[Step 5] Workflow Plan")
    planner = WorkflowPlannerAgent("WorkflowPlannerAgent", "Plan production workflow")
    plan = planner.run(script)

    print("\n[Step 6] Post Analysis")
    analyzer = PostAnalyzerAgent("PostAnalyzerAgent", "Analyze post quality or engagement")
    analysis = analyzer.run(script)

    return {
        "idea": ideas[0],
        "trends": trends,
        "persona_script": persona_script,
        "script": script,
        "workflow_plan": plan,
        "analysis": analysis
    }
