from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class BaseEvent(BaseModel):
    event_id: str
    timestamp: datetime
    service: str = "api-service"

class TaskEventPayload(BaseEvent):
    event_type: str  # task_created, task_completed
    task_id: int
    user_id: int
    meta: Optional[dict] = {}