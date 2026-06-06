from crewai import Agent
from core.config import OPENAI_API_KEY, MODEL

# Planner agent specialized in building structured, day-by-day travel itineraries.
# It uses the OpenAI model configured in core.config and runs in verbose mode
# so its reasoning is visible in the console/logs.
planner = Agent(
    role="Travel Planner",
    goal="Create a structured day-by-day itinerary",
    backstory="You are an expert travel planner who optimizes timing, travel, and rest.",
    llm=f"openai/{MODEL}",
    verbose=True
)
