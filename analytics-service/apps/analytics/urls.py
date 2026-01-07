from django.urls import path
from .views import UserStatsView

urlpatterns = [
    path('stats/users/', UserStatsView.as_view(), name='user-stats'),
]