-- name: insert_event
INSERT INTO analytics.events (event_id, event_type, task_id, user_id, timestamp, meta) VALUES

-- name: count_tasks_by_user
SELECT user_id, count() as total_tasks 
FROM analytics.events 
WHERE event_type = 'task_created' 
GROUP BY user_id