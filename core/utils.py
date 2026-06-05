from datetime import datetime
from typing import Tuple


def parse_dates(start: str, end: str) -> Tuple[datetime, datetime]:
    """
    Parse date strings in ISO format (YYYY-MM-DD) into datetime objects.
    """
    start_dt = datetime.strptime(start, "%Y-%m-%d")
    end_dt = datetime.strptime(end, "%Y-%m-%d")
    return start_dt, end_dt


def trip_duration(start: datetime, end: datetime) -> int:
    """
    Calculate the number of days between two dates (inclusive).
    """
    delta = end.date() - start.date()
    return max(delta.days + 1, 0)


def format_budget(amount: float) -> str:
    """
    Format a number into Indian Rupee style string: ₹40,000
    """
    formatted = f"{amount:,.0f}"
    return f"₹{formatted}"
