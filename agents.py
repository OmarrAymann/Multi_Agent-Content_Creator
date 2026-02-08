from crewai import Agent
from model_config import language_model


class ContentCalendarAgents:
    def __init__(self):
        self.model = language_model
    
    def brand_analyzer(self):
        return Agent(
            role='brand strategy analyst',
            goal='analyze brand voice, target audience, and content goals',
            backstory='expert in brand positioning and audience research with deep understanding of social media dynamics',
            verbose=False,
            allow_delegation=False,
            llm=self.model
        )
    
    def trend_researcher(self):
        return Agent(
            role='social media trend researcher',
            goal='identify trending topics, hashtags, and content opportunities',
            backstory='social media analyst specializing in viral content patterns and platform algorithms',
            verbose=False,
            allow_delegation=False,
            llm=self.model
        )
    
    def content_strategist(self):
        return Agent(
            role='content calendar strategist',
            goal='create strategic content calendar with posting schedule and themes',
            backstory='content strategy expert with experience planning social media campaigns for brands',
            verbose=False,
            allow_delegation=False,
            llm=self.model
        )
    
    def copywriter(self):
        return Agent(
            role='social media copywriter',
            goal='write engaging posts optimized for each platform',
            backstory='creative copywriter specialized in viral social media content and platform-specific formats',
            verbose=False,
            allow_delegation=False,
            llm=self.model
        )
    
    def calendar_packager(self):
        return Agent(
            role='content calendar compiler',
            goal='compile content calendar into professional html format with all posts and scheduling details',
            backstory='content operations specialist expert in organizing and presenting content calendars',
            verbose=False,
            allow_delegation=False,
            llm=self.model
        )
