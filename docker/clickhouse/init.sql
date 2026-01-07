CREATE DATABASE IF NOT EXISTS analytics;

CREATE TABLE IF NOT EXISTS analytics.events (
    event_id String,
    event_type String,
    task_id UInt32,
    user_id UInt32,
    timestamp DateTime,
    meta String
) ENGINE = MergeTree()
ORDER BY timestamp;