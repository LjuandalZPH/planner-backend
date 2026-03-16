from django.urls import path

from .views import GamificationHealthView

urlpatterns = [
    path("", GamificationHealthView.as_view(), name="gamification-health"),
]

