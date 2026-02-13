from django.urls import path
from .views import CoachOnlyView

urlpatterns = [
    path('coach-only/', CoachOnlyView.as_view(), name='coach-only'),
]
