from django.urls import path

from .views import MissionsHealthView

urlpatterns = [
    path("", MissionsHealthView.as_view(), name="missions-health"),
]

