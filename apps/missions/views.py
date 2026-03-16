from rest_framework.response import Response
from rest_framework.views import APIView

from .services import ping


class MissionsHealthView(APIView):
    authentication_classes: list = []
    permission_classes: list = []

    def get(self, request):
        return Response({"message": f"Missions API funcionando correctamente ({ping()})."})

