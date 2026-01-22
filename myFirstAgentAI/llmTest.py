# Example using CrewAI with Gemini API (simplified)
import os
from crewai import Agent, Task, Crew
from langchain_google_genai import ChatGoogleGenerativeAI

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")  # or "GENAI_API_KEY" or GOOGLE_API_KEY

# print(GOOGLE_API_KEY)

# 1. Set up your free LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY  # Get from Google AI Studio
)

print(llm)

# 2. Create an agent
researcher = Agent(
    role='Senior Research Analyst',
    goal='Find and analyze the latest AI news',
    backstory="You're an expert researcher...",
    llm=llm,
    verbose=True
)

# 3. Create a task
research_task = Task(
    # description='Find 3 recent breakthroughs in AI agents from the past month',
    description='Find ways from Philadelphia to Boston',
    agent=researcher,
    expected_output='A bulleted list with summaries'
)

# 4. Create the crew
crew = Crew(
    agents=[researcher],
    tasks=[research_task]
)

# 5. Execute
result = crew.kickoff()
print(result)
