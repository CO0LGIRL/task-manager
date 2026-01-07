from clickhouse_driver import Client
from django.conf import settings

class ClickHouseClient:
    def __init__(self):
        self.client = Client(**settings.CLICKHOUSE_CONFIG)

    def insert_event(self, event_data: dict):
        import json
        
        # SQL Insert
        query = 'INSERT INTO analytics.events (event_id, event_type, task_id, user_id, timestamp, meta) VALUES'
        
        data = [{
            'event_id': event_data['event_id'],
            'event_type': event_data['event_type'],
            'task_id': event_data['task_id'],
            'user_id': event_data['user_id'],
            'timestamp': event_data['timestamp'],
            'meta': json.dumps(event_data.get('meta', {}))
        }]
        
        self.client.execute(query, data)

    def get_user_stats(self):
        query = """
            SELECT user_id, count() as tasks_count 
            FROM analytics.events 
            WHERE event_type = 'task_created'
            GROUP BY user_id
        """
        return self.client.execute(query)

db = ClickHouseClient()