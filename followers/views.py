from rest_framework import generics, permissions
from .models import Follower
from .serializer import FollowerSerializer
from drf_api.permissions import IsOwnerOrReadOnly
# Create your views here.
class FollowList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowerSerializer

    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FollowDetails(generics.RetrieveDestroyAPIView):
    # permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowerSerializer

    queryset = Follower.objects.all()