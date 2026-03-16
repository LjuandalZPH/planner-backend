from django.urls import path

from .views import UsersHealthView

urlpatterns = [
    path("", UsersHealthView.as_view(), name="users-health"),
]

