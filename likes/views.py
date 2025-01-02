from rest_framework import generics, permissions
from .models import Likes
from .serializer import LikeSerializer
from drf_api.permissions import IsOwnerOrReadOnly
# Create your views here.
class LikeList(generics.ListCreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Likes.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikeDetails(generics.RetrieveDestroyAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Likes.objects.all()
        