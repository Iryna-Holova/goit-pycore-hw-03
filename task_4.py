"""Task 4: Upcoming birthdays"""

from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list) -> list:
    """
    Calculate upcoming birthdays within a week for a given list of users.

    Args:
        users (list): A list of dictionaries containing user information with
        keys "name" and "birthday".

    Returns:
        list: A list of dictionaries with "name" and "congratulation_date"
        keys for upcoming birthdays within a week.
    """
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        if (birthday_this_year - today).days < 7:
            if birthday_this_year.weekday() >= 5:
                congratulation_date = birthday_this_year + timedelta(
                    days=(7 - birthday_this_year.weekday())
                )
            else:
                congratulation_date = birthday_this_year

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays
