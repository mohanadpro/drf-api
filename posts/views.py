from rest_framework import permissions, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from .models import Post
from .serializer import PostSerializer
from drf_api.permissions import IsOwnerOrReadOnly
# Create your views here.
class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Post.objects.annotate(
        comments_count = Count('likes', distinct=True),
        likes_count = Count('comment', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title'
    ]

    ordering_fields = [
        'comments_count',
        'likes_count',
        'likes_created_at'
    ]



    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class Post_Details(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer

    queryset = Post.objects.all()
        