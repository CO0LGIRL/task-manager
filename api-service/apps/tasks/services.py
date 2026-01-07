import uuid
from .models import Task
from apps.events.producer import producer
from common.schemas.analytics import TaskEventPayload
from common.utils.time import current_utc_time

def create_task(title: str, user_id: int) -> Task:
    task = Task.objects.create(title=title, assignee_id=user_id)
    
    event = TaskEventPayload(
        event_id=str(uuid.uuid4()),
        timestamp=current_utc_time(),
        event_type="task_created",
        task_id=task.id,
        user_id=user_id,
        meta={"title": title}
    )
    
    producer.send_event('analytics_events', event.dict(exclude_none=True, by_alias=True))
    
    return task