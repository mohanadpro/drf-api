from rest_framework import permissions, generics
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import CommentSerializer
from .models import Comment

# Create your views here.

class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_fields = [
        'post'
    ]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Comment.objects.all()