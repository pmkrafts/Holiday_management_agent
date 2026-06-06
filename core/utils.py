from datetime import datetime
from typing import Tuple


def parse_dates(start: str, end: str) -> Tuple[datetime, datetime]:
    """Parse date strings in ISO format (YYYY-MM-DD) into datetime objects.

    Args:
        start: Start date string in YYYY-MM-DD format.
        end: End date string in YYYY-MM-DD format.

    Returns:
        A tuple of (start_datetime, end_datetime) at midnight.
    """
    start_dt = datetime.strptime(start, "%Y-%m-%d")
    end_dt = datetime.strptime(end, "%Y-%m-%d")
    return start_dt, end_dt


def trip_duration(start: datetime, end: datetime) -> int:
    """Calculate the number of days between two dates (inclusive).

    Args:
        start: Starting datetime.
        end: Ending datetime.

    Returns:
        Total number of days covered by the trip, minimum zero.
    """
    delta = end.date() - start.date()
    # Add 1 so same start and end counts as a 1-day trip; guard against negative spans.
    return max(delta.days + 1, 0)


def format_budget(amount: float) -> str:
    """Format a number into Indian Rupee style string: ₹40,000

    Args:
        amount: Numeric budget value.

    Returns:
        A formatted currency string with the Indian Rupee symbol.
    """
    formatted = f"{amount:,.0f}"
    return f"₹{formatted}"
