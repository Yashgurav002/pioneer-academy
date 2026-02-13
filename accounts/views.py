from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsCoach


class CoachOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsCoach]

    def get(self, request):
        return Response({"message": "Hello Coach!"})
