from agents.base_agent import BaseAgent

class SchedulerAgent(BaseAgent):
    def __init__(self , name : str  = "" , prompt : str = ""):
        self.name="SchedulerAgent",
        self.prompt="You are a social media content scheduling assistant. Your job is to create optimized weekly content calendars based on input content types, frequency, and platform best practices."
      
        super().__init__(
            name,
            prompt      )

    def generate_schedule(self, content_types, frequency="daily", platforms=["Instagram", "YouTube"], timezone="IST", goals="growth and engagement"):
        prompt = f"""
Generate a detailed weekly content posting schedule.

Content Types: {", ".join(content_types)}
Frequency: {frequency}
Platforms: {", ".join(platforms)}
Timezone: {timezone}
Goals: {goals}

For each day, list:
- Platform
- Content Type
- Ideal Posting Time
- Caption Theme or CTA (if relevant)
"""
        return self.run(prompt)
