from datetime import datetime


def parse_date(date: str) -> datetime:
    return datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
