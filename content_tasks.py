from crewai import Task


class ContentCalendarTasks:
    def analyze_brand(self, agent, brand_input):
        return Task(
            description=f"""
            analyze the brand and create comprehensive brand profile.
            
            extract and define:
            1. brand voice and tone
            2. target audience demographics
            3. content pillars and themes
            4. brand values and messaging
            5. competitor analysis
            
            brand information: {brand_input}
            
            format output as detailed brand profile with clear guidelines.
            """,
            agent=agent,
            expected_output="comprehensive brand profile with voice guidelines and audience insights"
        )
    
    def research_trends(self, agent, context):
        return Task(
            description="""
            research current social media trends and opportunities.
            
            identify:
            1. trending topics relevant to brand niche
            2. popular hashtags and keywords
            3. viral content formats
            4. seasonal opportunities and events
            5. content gaps in the market
            
            provide specific trend insights with examples.
            """,
            agent=agent,
            context=context,
            expected_output="trend research report with actionable content opportunities"
        )
    
    def create_strategy(self, agent, context):
        return Task(
            description="""
            develop strategic content calendar framework.
            
            create:
            1. content themes for each week
            2. posting frequency per platform
            3. content mix ratios
            4. optimal posting times
            5. content series and campaigns
            
            organize into monthly calendar structure with clear schedule.
            """,
            agent=agent,
            context=context,
            expected_output="strategic content calendar framework with themes and schedule"
        )
    
    def write_content(self, agent, context):
        return Task(
            description="""
            write 30+ social media posts for the content calendar.
            
            create posts for each platform:
            - linkedin: professional insights
            - twitter: quick tips and threads
            - instagram: visual captions
            - facebook: community engagement
            - tiktok: trending formats
            
            each post must include:
            - platform-optimized copy
            - suggested hashtags
            - call to action
            - best posting time
            - content type
            
            write minimum 30 complete posts covering full month.
            """,
            agent=agent,
            context=context,
            expected_output="30+ platform-optimized social media posts with hashtags and timing"
        )
    
    def package_calendar(self, agent, context):
        return Task(
            description="""
create a complete 30-day social media content calendar.

compile all the content into a structured format with:

BRAND INFORMATION:
- brand name
- month and year
- total statistics (30+ posts, number of platforms, posts per week, content themes count)

CONTENT PILLARS (4-6 pillars):
for each pillar provide:
- pillar name
- description

30+ SOCIAL MEDIA POSTS:
for each post provide:
- post number (1-30+)
- platform (linkedin, twitter, instagram, facebook, or tiktok)
- post title (catchy and engaging)
- full post content (minimum 50 words, engaging copy)
- 5-10 relevant hashtags
- posting day (monday-sunday)
- posting time (specific time like 9:00 AM)
- content type (educational, promotional, entertaining, etc)

HASHTAG BANK:
- list of 20-30 relevant hashtags for the brand

POSTING SCHEDULE:
for each platform provide:
- platform name
- posting frequency (daily, 3x week, etc)
- best posting times
- content type focus

KPI TARGETS (6-8 metrics):
- metric name
- target value

organize everything clearly and make sure all 30+ posts are complete with engaging content that matches the brand voice and goals.
            """,
            agent=agent,
            context=context,
            expected_output="complete organized content calendar with brand info, 30+ detailed posts with full content and hashtags, content pillars, hashtag bank, posting schedule, and KPI targets"
        )