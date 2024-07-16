"""Task 1: Date difference"""

from datetime import datetime


def get_days_from_today(date: str) -> int | None:
    """
    Calculate the number of days between today and the given date.

    Args:
        date (str): Date in 'YYYY-MM-DD' format.

    Returns:
        int: Number of days between today and the given date. If the date
        format is incorrect, returns None.
    """
    try:
        target_date = datetime.strptime(date, '%Y-%m-%d').date()
        current_date = datetime.today().date()
        return (current_date - target_date).days
    except ValueError:
        print('Wrong date format. Use "YYYY-MM-DD".')
        return None
