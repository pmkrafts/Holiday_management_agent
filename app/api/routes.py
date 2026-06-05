from fastapi import APIRouter, HTTPException
from schema.trips import TripRequest
from agents.crew import HolidayCrew

router = APIRouter()

@router.post("/plan_trip")
def create_plan(request: TripRequest):
    try:
        crew = HolidayCrew()
        result = crew.kickoff(request.dict())
        return {"itinerary": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
