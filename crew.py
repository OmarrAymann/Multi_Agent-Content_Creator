from crewai import Crew, Process
from agents import ContentCalendarAgents
from content_tasks import ContentCalendarTasks
import os

os.environ["CREWAI_TELEMETRY_ENABLED"] = "false"


class ContentCalendarCrew:
    def __init__(self):
        self.agents = ContentCalendarAgents()
        self.tasks = ContentCalendarTasks()
    
    def build_crew(self, brand_input):
        brand_analyst = self.agents.brand_analyzer()
        trend_researcher = self.agents.trend_researcher()
        strategist = self.agents.content_strategist()
        writer = self.agents.copywriter()
        packager = self.agents.calendar_packager()
        
        brand_task = self.tasks.analyze_brand(
            agent=brand_analyst,
            brand_input=brand_input
        )
        
        trend_task = self.tasks.research_trends(
            agent=trend_researcher,
            context=[brand_task]
        )
        
        strategy_task = self.tasks.create_strategy(
            agent=strategist,
            context=[brand_task, trend_task]
        )
        
        content_task = self.tasks.write_content(
            agent=writer,
            context=[brand_task, trend_task, strategy_task]
        )
        
        calendar_task = self.tasks.package_calendar(
            agent=packager,
            context=[brand_task, trend_task, strategy_task, content_task]
        )
        
        return Crew(
            agents=[brand_analyst, trend_researcher, strategist, writer, packager],
            tasks=[brand_task, trend_task, strategy_task, content_task, calendar_task],
            process=Process.sequential,
            verbose=False
        )
    
    def execute(self, brand_input):
        crew = self.build_crew(brand_input)
        result = crew.kickoff()
        return result
