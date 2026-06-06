from pydantic import BaseModel
from typing import Optional

class TripRequest(BaseModel):
    destination: str
    start_date: str
    end_date: str
    budget: float
    travelers: int
    interests: Optional[str] = ""

class TripResponse(BaseModel):
    raw: str
    markdown: str
    saved_to: Optional[str] = None