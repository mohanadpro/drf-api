from django.urls import path
from .views import PostList, Post_Details
urlpatterns = [
    path('',PostList.as_view()),
    path('<int:pk>',Post_Details.as_view())
]