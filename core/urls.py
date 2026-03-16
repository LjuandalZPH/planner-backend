from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path


def healthcheck_view(request):
    return HttpResponse("Planner backend funcionando correctamente.")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("apps.users.urls")),
    path("api/missions/", include("apps.missions.urls")),
    path("api/gamification/", include("apps.gamification.urls")),
    path("", healthcheck_view, name="healthcheck"),
]

