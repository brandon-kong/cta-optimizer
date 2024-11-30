from datetime import datetime


def is_rush_period():
    """
    Return True if it is rush period.

    According to CTA, rush periods are from 5-9:10 AM and 2-6:18 PM on weekdays.
    """
    now = datetime.now()
    if now.weekday() < 5:
        return (5 <= now.hour < 9 and now.minute < 10) or (
            14 <= now.hour < 18 and now.minute < 18
        )
    return False
