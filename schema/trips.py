from pydantic import BaseModel
from typing import Optional


# Pydantic models that define the request and response shapes for the /plan_trip endpoint.


class TripRequest(BaseModel):
    """Payload sent by the client when requesting a new trip plan."""
    destination: str       # City, state, or country the user wants to visit.
    start_date: str        # Trip start date in YYYY-MM-DD format.
    end_date: str          # Trip end date in YYYY-MM-DD format.
    budget: float          # Estimated budget in Indian Rupees (₹).
    travelers: int         # Number of people traveling together.
    interests: Optional[str] = ""  # Free-text preferences, e.g., "beach, trekking, food".


class TripResponse(BaseModel):
    """Payload returned by the server after the crew generates an itinerary."""
    raw: str               # Plain-text version of the itinerary (Markdown stripped).
    markdown: str          # Original Markdown-formatted itinerary from the crew.
    saved_to: Optional[str] = None  # Local file path where the plan was saved, if any.
