# -------------------------
# research_agent.py
# Example of a multi-agent research system using CrewAI and Google Gemini LLM
# will generate draft_report.md, final_output.md, final_report.md and research_notes.md after successful executed
# -------------------------
import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, WebsiteSearchTool, ScrapeWebsiteTool
from langchain_google_genai import ChatGoogleGenerativeAI

# ========================
# 1. SETUP & CONFIGURATION
# ========================

# os.environ["GOOGLE_API_KEY"] = "Your API Key Here"  # Replace this! if you not using env variables
GOOGLE_API_KEY = os.environ.get("GENAI_API_KEY")
print(GOOGLE_API_KEY)

# ========================
# 2. TOOLS FOR THE AGENT
# ========================
# For better results, you can use SerperDevTool (100 free searches/month at serper.dev)
search_tool = SerperDevTool()  # Or use DuckDuckGoSearchTool() from crewai_tools

# Create web scraping tool
scrape_tool = ScrapeWebsiteTool()

# ========================
# 3. DEFINE THE LLM (BRAIN)
#    Run llmTest.py to verify your setup
# ========================

# Using Google Gemini 2.5 Flash - FREE TIER, comfirm with your application
llm = ChatGoogleGenerativeAI(
    # model="gemini-1.5-flash",  # Free and capable
    model="gemini-2.5-flash",
    temperature=0.7,
    google_api_key=GOOGLE_API_KEY
)

# ========================
# 4. CREATE THE AGENTS
# ========================

# Agent 1: Research Specialist
research_specialist = Agent(
    role='Senior Research Analyst',
    goal='Find the most relevant and recent information on any given topic',
    backstory="""You are an expert researcher with 15 years of experience in data analysis 
    and information synthesis. You have worked at top research institutions and know how to 
    find credible information quickly. You're meticulous and thorough.""",
    tools=[search_tool, scrape_tool],  # Tools this agent can use
    llm=llm,
    verbose=True,  # Shows what the agent is thinking
    allow_delegation=False  # This agent works independently
)

# Agent 2: Content Strategist
content_strategist = Agent(
    role='Content Strategy Director',
    goal='Transform research findings into compelling, well-structured reports',
    backstory="""You are a former journalist turned content strategist. You have a knack 
    for turning complex information into engaging, easy-to-understand content. You've 
    written for Forbes, TechCrunch, and Harvard Business Review.""",
    tools=[],  # This agent doesn't need search tools
    llm=llm,
    verbose=True,
    allow_delegation=False
)

# Agent 3: Quality Assurance Editor
quality_editor = Agent(
    role='Quality Assurance Editor',
    goal='Ensure the final report is accurate, well-structured, and professional',
    backstory="""You are a meticulous editor with 10 years of experience at academic 
    publishing houses. You catch factual inaccuracies, improve flow, and ensure 
    citations are properly formatted. Nothing gets past your critical eye.""",
    tools=[search_tool],  # Can double-check facts
    llm=llm,
    verbose=True,
    allow_delegation=False
)

# ========================
# 5. CREATE THE TASKS
# ========================

# Task 1: Research the topic
research_task = Task(
    description="""Research the following topic: '{topic}'

    Your research MUST be:
    1. Recent (prioritize information from the last 6 months)
    2. From credible sources (academic papers, official blogs, reputable news)
    3. Comprehensive (cover different perspectives)
    4. Well-documented (save URLs for citations)

    Search for:
    - Latest developments
    - Key players/companies
    - Technical specifications if applicable
    - Market trends
    - Challenges and limitations
    - Future predictions

    Return your findings in a detailed research notes format.""",
    expected_output="""A comprehensive research document containing:
    1. Executive summary of findings
    2. Key facts and data points (with sources)
    3. Recent developments (last 6 months)
    4. Different perspectives on the topic
    5. List of credible sources with URLs
    6. Gaps in current knowledge/research""",
    agent=research_specialist,
    output_file="research_notes.md"  # Saves output to file
)

# Task 2: Write the report
writing_task = Task(
    description="""Using the research notes provided, create a professional report on '{topic}'.

    Structure the report as follows:
    1. Title Page
    2. Executive Summary (1 paragraph)
    3. Introduction
    4. Current State Analysis
    5. Recent Developments
    6. Key Players/Innovations
    7. Challenges and Limitations
    8. Future Outlook
    9. Conclusion
    10. References

    Make the report engaging but professional. Use markdown formatting with headers, bullet points, and bold text for emphasis.""",
    expected_output="A well-structured, professional report in markdown format, 1000-1500 words, with proper citations.",
    agent=content_strategist,
    context=[research_task],  # This task depends on research_task being completed
    output_file="draft_report.md"
)

# Task 3: Review and improve
review_task = Task(
    description="""Review the draft report on '{topic}' for:
    1. Factual accuracy (verify at least 3 key claims)
    2. Logical flow and structure
    3. Grammar and spelling
    4. Citation consistency
    5. Professional tone
    6. Clear takeaways

    Make necessary improvements and create a final polished version.
    If you find questionable facts, use the search tool to verify them.""",
    expected_output="A polished, publication-ready report with all corrections made and a summary of changes.",
    agent=quality_editor,
    context=[writing_task],  # Depends on the writing task
    output_file="final_report.md"
)

# ========================
# 6. CREATE THE CREW & KICKOFF
# ========================

# Define the crew (team of agents)
crew = Crew(
    agents=[research_specialist, content_strategist, quality_editor],
    tasks=[research_task, writing_task, review_task],
    process=Process.sequential,  # Tasks run one after another
    verbose=True  # Detailed output
)

# ========================
# 7. EXECUTE THE AGENT
# ========================

if __name__ == "__main__":
    print("Starting Research Agent...")
    print("=" * 50)

    # Define your research topic here
    # research_topic = "AI Agents in Healthcare in 2024"  # ⬅️ CHANGE THIS TO ANY TOPIC
    research_topic = "The ways from Philadelphia to Boston"  # ⬅️ CHANGE THIS TO ANY TOPIC

    # Update tasks with the topic
    research_task.description = research_task.description.format(topic=research_topic)
    writing_task.description = writing_task.description.format(topic=research_topic)
    review_task.description = review_task.description.format(topic=research_topic)

    # Start the crew!
    result = crew.kickoff(inputs={'topic': research_topic})

    print("\n" + "=" * 50)
    print("Research Complete!")
    print(f"Topic: {research_topic}")
    print("=" * 50)

    # Display the final result
    print("\nFINAL REPORT:")
    print("=" * 50)
    print(result)

    # Save the final result
    with open("final_output.md", "w") as f:
        f.write(str(result))

    print("Files saved:")
    print("research_notes.md (raw research)")
    print("draft_report.md (first draft)")
    print("final_report.md (polished version)")
    print("final_output.md (this output)")
