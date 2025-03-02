import pandas as pd


def format_timestamp(timestamp: str) -> str:
    return pd.to_datetime(timestamp).strftime('%d-%m-%Y %H:%M:%S')


def format_duration(seconds: int) -> str:
    minutes = int(seconds // 60)
    remaining_seconds = int(seconds % 60)
    return f'{minutes:02d}:{remaining_seconds:02d}'
