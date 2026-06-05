from crewai import Agent
from core.config import OPENAI_API_KEY, MODEL

planner = Agent(
    role="Travel Planner",
    goal="Create a structured day-by-day itinerary",
    backstory="You are an expert travel planner who optimizes timing, travel, and rest.",
    llm=f"openai/{MODEL}",
    verbose=True
)