from rest_framework.views import APIView
from rest_framework.response import Response
from .services import analytics_service

class UserStatsView(APIView):
    def get(self, request):
        data = analytics_service.get_tasks_by_user()
        return Response(data)