from django.test import SimpleTestCase
from unittest.mock import patch, MagicMock
from apps.analytics.services import AnalyticsService

class AnalyticsServiceTest(SimpleTestCase):
    
    @patch('apps.analytics.models.ClickHouseClient')
    def test_get_tasks_by_user(self, MockDb):
        mock_client_instance = MockDb.return_value
        mock_client_instance.client.execute.return_value = [(1, 5), (2, 3)]
        
        from apps.analytics import services
        services.db = mock_client_instance

        service = AnalyticsService()
        result = service.get_tasks_by_user()

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['user_id'], 1)
        self.assertEqual(result[0]['total_tasks'], 5)