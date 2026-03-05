from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from profiles.models import CoachProfile
from accounts.permissions import IsAdmin
from .serializers import CoachReadSerializer, CoachWriteSerializer
from rest_framework.response import Response
from rest_framework import status


class CoachProfileViewSet(viewsets.ModelViewSet):
    queryset = CoachProfile.objects.select_related('profile__user')
    permission_classes = [IsAuthenticated, IsAdmin]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CoachReadSerializer
        return CoachWriteSerializer

    def create(self, request, *args, **kwargs):
        write_serializer = self.get_serializer(data=request.data)
        write_serializer.is_valid(raise_exception=True)
        coach_profile = write_serializer.save()

        # Use read serializer for response
        read_serializer = CoachReadSerializer(coach_profile)

        return Response(read_serializer.data, status=status.HTTP_201_CREATED)