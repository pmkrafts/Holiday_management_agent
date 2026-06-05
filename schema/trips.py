from pydantic import BaseModel
from typing import Optional

class TripRequest(BaseModel):
    destination: str
    start_date: str
    end_date: str
    budget: float
    travelers: int
    interests: Optional[str] = ""