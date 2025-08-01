# pipeline_v3.py
from agents.Ideation_agent import Ideation_Agent
from agents.trend_hunter_agent import TrendHunterAgent
from agents.Persona_agent import PersonaAgent
from agents.scripting_agent import ScriptingAgent
from agents.workflow_planner_agent import WorkflowPlannerAgent
from agents.post_analyzer_agent import PostAnalyzerAgent
from agents.engagement_agent import EngagementAgent
from agents.seo_agent import SEOAgent
from agents.scheduler_agent import SchedulerAgent
from agents.multimodal_agent import MultimodalAgent
from agents.correction_agent import CorrectionAgent
from agents.memory_agent import MemoryAgent
from agents.goal_agent import GoalAgent
from agents.passing_agent import PassingAgent
from agents.self_correction_agent import SelfCorrectionAgent

def run_pipeline_v3(topic: str):
    print("Step 1 \n")
    memory_agent = MemoryAgent("MemoryAgent", "Recall past topics or preferences")
    memory_context = memory_agent.run(topic)
    
    print("Step 2 \n")
    goal_agent = GoalAgent("GoalAgent", "Define long-term goals")
    goals = goal_agent.run(topic)
    memory_agent.store("GoalAgent", goals, metadata={"input": topic})
    
    print("Step 3 \n")
    idea_agent = Ideation_Agent("IdeationAgent", "Generate ideas")
    ideas = idea_agent.run(f"{topic}\nContext: {memory_context}")
    memory_agent.store("IdeationAgent", ideas, metadata={"input": topic})
    
    print("Step 4 \n")
    trend_agent = TrendHunterAgent("TrendHunterAgent", "Analyze trends")
    trends = trend_agent.run(topic)
    memory_agent.store("TrendHunterAgent", trends)
    
    print("Step 5 \n")
    enriched_idea_input = f"Idea: {ideas[0]['description']}\nTrends: {trends}"
    
    print("Step 6 \n")
    persona_agent = PersonaAgent("PersonaAgent", "Apply Gen Z tone")
    
    print("Step 7 \n")
    adjusted_idea = persona_agent.run(enriched_idea_input)
    memory_agent.store("PersonaAgent", adjusted_idea)
    
    print("Step 8 \n")
    script_agent = ScriptingAgent("ScriptAgent", "Generate content script")
    script = script_agent.run(adjusted_idea)
    memory_agent.store("ScriptingAgent", script)
    
    print("Step 9 \n")
    planner = WorkflowPlannerAgent("WorkflowPlannerAgent", "Plan production steps")
    plan = planner.run(script)
    memory_agent.store("WorkflowPlannerAgent", plan)
    
    print("Step 10 \n")
    analyzer = PostAnalyzerAgent("PostAnalyzerAgent", "Evaluate content quality")
    analysis = analyzer.run(script)
    memory_agent.store("PostAnalyzerAgent", analysis)
    
    print("Step 11 \n")
    seo_agent = SEOAgent("SEOAgent", "Optimize for search")
    seo_script = seo_agent.run(script)
    memory_agent.store("SEOAgent", seo_script)
    
    print("Step 12 \n")
    engagement_agent = EngagementAgent("EngagementAgent", "Enhance for engagement")
    engagement_script = engagement_agent.run(seo_script)
    memory_agent.store("EngagementAgent", engagement_script)
    
    print("Step 13 \n")
    scheduler_agent = SchedulerAgent("SchedulerAgent", "Schedule the post")
    schedule = scheduler_agent.run(engagement_script)
    memory_agent.store("SchedulerAgent", schedule)
    
    print("Step 14 \n")
    multimodal_agent = MultimodalAgent("MultimodalAgent", "Generate visuals")
    visual_assets = multimodal_agent.run(engagement_script)
    memory_agent.store("MultimodalAgent", visual_assets)
    
    print("Step 15 \n")
    correction_agent = CorrectionAgent("CorrectionAgent", "Suggest content fixes")
    corrected_script = correction_agent.run(f"{engagement_script}\nAnalysis: {analysis}")
    memory_agent.store("CorrectionAgent", corrected_script)
    
    print("Step 16 \n")
    self_correction = SelfCorrectionAgent("SelfCorrectionAgent", "Improve reasoning")
    improved_script = self_correction.run(previous_output=corrected_script, context=goals)
    memory_agent.store("SelfCorrectionAgent", improved_script)
    
    print("Step 17 \n")
    passing_agent = PassingAgent("PassingAgent", "Connect agent outputs")
    final_package = passing_agent.run({
        "script": improved_script,
        "visuals": visual_assets,
        "schedule": schedule,
        "workflow_plan": plan,
        "goals": goals
    })

    return final_package
