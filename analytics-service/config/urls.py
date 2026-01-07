from django.urls import path, include

urlpatterns = [
    path('api/v1/analytics/', include('apps.analytics.urls')),
]