from crewai import Agent
from core.config import OPENAI_API_KEY, MODEL

researcher = Agent(
    role="Travel Researcher",
    goal="Verify facts about destinations",
    backstory="You check opening hours, travel times, weather, events, and safety.",
    llm=f"openai/{MODEL}",
    verbose=True
)