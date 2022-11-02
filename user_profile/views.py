from rest_framework import viewsets, permissions

from .serializers import ProfileSerializer
from .models import UserProfile
from .permission import IsOwnerOrReadOnly


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
