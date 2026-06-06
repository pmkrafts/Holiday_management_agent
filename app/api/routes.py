import re
from fastapi import APIRouter, HTTPException
from schema.trips import TripRequest, TripResponse
from agents.crew import HolidayCrew, CrewExecutionError

router = APIRouter()

def _markdown_to_raw(text: str) -> str:
    """Strip basic Markdown syntax for a plain-text version."""
    raw = re.sub(r"#+\s*", "", text)
    raw = re.sub(r"\*\*|__", "", raw)
    raw = re.sub(r"\*|_", "", raw)
    raw = re.sub(r"`{1,3}", "", raw)
    raw = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", raw)
    raw = re.sub(r"!\[([^\]]*)\]\([^\)]+\)", r"\1", raw)
    raw = re.sub(r">\s*", "", raw)
    raw = re.sub(r"-{3,}|_{3,}|\*{3,}", "", raw)
    return raw.strip()

@router.post("/plan_trip", response_model=TripResponse)
def create_plan(request: TripRequest):
    try:
        crew = HolidayCrew()
        result, saved_path = crew.kickoff(request.model_dump())
        markdown = str(result)
        raw = _markdown_to_raw(markdown)
        return TripResponse(raw=raw, markdown=markdown, saved_to=saved_path)
    except CrewExecutionError as e:
        raise HTTPException(status_code=503, detail=f"Agent execution failed: {e}")
    except ValueError as e:
        raise HTTPException(status_code=422, detail=f"Invalid input: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")
