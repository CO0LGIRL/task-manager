from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from unittest.mock import patch

class TaskAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.force_authenticate(user=self.user)

    @patch('apps.events.producer.EventProducer.send_event')
    def test_create_task_sends_event(self, mock_send_event):
        data = {'title': 'Buy milk'}
        response = self.client.post('/api/v1/tasks/', data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Buy milk')
        
        mock_send_event.assert_called_once()
        
        args, _ = mock_send_event.call_args
        self.assertEqual(args[0], 'analytics_events')
        self.assertEqual(args[1]['event_type'], 'task_created')