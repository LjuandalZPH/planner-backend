from rest_framework.response import Response
from rest_framework.views import APIView

from .services import ping


class GamificationHealthView(APIView):
    authentication_classes: list = []
    permission_classes: list = []

    def get(self, request):
        return Response(
            {"message": f"Gamification API funcionando correctamente ({ping()})."}
        )

