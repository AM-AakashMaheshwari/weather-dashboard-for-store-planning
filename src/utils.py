from datetime import datetime
from zoneinfo import ZoneInfo

# Use IANA tz; tzdata package makes this work cross-platform
IST = ZoneInfo("Asia/Kolkata")

def now_ist() -> datetime:
    return datetime.now(IST)

def yyyymmdd(dt: datetime) -> str:
    return dt.strftime("%Y%m%d")

def iso_local(dt: datetime) -> str:
    return dt.isoformat(timespec="seconds")
