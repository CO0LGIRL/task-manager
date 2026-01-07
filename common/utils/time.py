from django.utils import timezone
from datetime import datetime

def current_utc_time() -> datetime:
    return timezone.now()