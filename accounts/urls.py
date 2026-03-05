from django.urls import path
from .views import CoachOnlyView, PlayerOnlyView

urlpatterns = [
    path('coach-only/', CoachOnlyView.as_view(), name='coach-only'),
    path('player-only/', PlayerOnlyView.as_view(), name='player-only'),

]
