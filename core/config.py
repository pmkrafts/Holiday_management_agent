from dotenv import load_dotenv
import os

# Load environment variables from a .env file at project startup.
# This allows secrets like OPENAI_API_KEY to be kept out of source control.
load_dotenv()

# API key used by CrewAI/OpenAI-backed agents. Must be set in the environment or .env file.
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Default OpenAI model used by the planner and researcher agents.
# Change this to switch to a different model (e.g., "gpt-4o", "gpt-3.5-turbo").
MODEL = "gpt-4o-mini"
