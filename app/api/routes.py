import re
from fastapi import APIRouter, HTTPException
from schema.trips import TripRequest, TripResponse
from agents.crew import HolidayCrew, CrewExecutionError

# Router that groups the trip-planning endpoints under a common prefix.
router = APIRouter()


def _markdown_to_raw(text: str) -> str:
    """Strip basic Markdown syntax for a plain-text version.

    Removes headings, bold/italic/emphasis markers, inline/fenced code markers,
    links, images, blockquotes, and horizontal rules so the output is readable
    as raw text.
    """
    raw = re.sub(r"#+\s*", "", text)          # Remove heading markers and trailing space.
    raw = re.sub(r"\*\*|__", "", raw)         # Remove bold markers.
    raw = re.sub(r"\*|_", "", raw)            # Remove italic/emphasis markers.
    raw = re.sub(r"`{1,3}", "", raw)          # Remove inline and fenced code backticks.
    raw = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", raw)  # Replace [text](url) with just text.
    raw = re.sub(r"!\[([^\]]*)\]\([^\)]+\)", r"\1", raw)  # Replace ![alt](url) with alt text.
    raw = re.sub(r">\s*", "", raw)           # Remove blockquote markers.
    raw = re.sub(r"-{3,}|_{3,}|\*{3,}", "", raw)  # Remove horizontal rules.
    return raw.strip()


@router.post("/plan_trip", response_model=TripResponse)
def create_plan(request: TripRequest):
    """Accept trip details, run the AI crew, and return the itinerary in two formats.

    Returns:
        TripResponse containing a raw-text version, the original Markdown version,
        and the local file path where the plan was persisted (if saving succeeded).
    """
    try:
        # Delegate planning and verification to the HolidayCrew agents.
        crew = HolidayCrew()
        result, saved_path = crew.kickoff(request.model_dump())

        # Convert the crew result into both Markdown and plain-text representations.
        markdown = str(result)
        raw = _markdown_to_raw(markdown)

        return TripResponse(raw=raw, markdown=markdown, saved_to=saved_path)
    except CrewExecutionError as e:
        # Crew-level failures (agent loop failures, tool errors, etc.) map to 503.
        raise HTTPException(status_code=503, detail=f"Agent execution failed: {e}")
    except ValueError as e:
        # Validation problems with the request payload map to 422.
        raise HTTPException(status_code=422, detail=f"Invalid input: {e}")
    except Exception as e:
        # Catch-all for unexpected server-side errors.
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")
