import os
from pathlib import Path
from .models import db

class AnalyticsService:
    def __init__(self):
        self.queries = self._load_queries()

    def _load_queries(self) -> dict:
        queries = {}
        path = Path(__file__).parent / 'queries.sql'
        
        with open(path, 'r') as f:
            raw = f.read().split('-- name: ')
            for chunk in raw:
                if not chunk.strip(): 
                    continue
                name, query = chunk.split('\n', 1)
                queries[name.strip()] = query.strip()
        return queries

    def get_tasks_by_user(self):
        query = self.queries.get('count_tasks_by_user')
        if not query:
            raise ValueError("Query 'count_tasks_by_user' not found")
            
        result = db.client.execute(query)
        return [{"user_id": row[0], "total_tasks": row[1]} for row in result]

analytics_service = AnalyticsService()