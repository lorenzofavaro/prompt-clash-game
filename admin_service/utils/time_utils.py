from datetime import datetime
from datetime import timezone
from zoneinfo import ZoneInfo


def minutes_and_seconds_to_seconds(minutes: int, seconds: int) -> int:
    return minutes * 60 + seconds


def convert_to_non_utc_time(time_str: str) -> str:
    if time_str.endswith('Z'):
        utc_time = datetime.fromisoformat(time_str.replace('Z', '+00:00'))
    else:
        utc_time = datetime.fromisoformat(time_str).replace(tzinfo=timezone.utc)
    local_time = utc_time.astimezone(ZoneInfo('Europe/Rome'))
    return local_time.isoformat()
