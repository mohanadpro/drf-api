from django.urls import path
from .views import CommentList, CommentDetails
urlpatterns = [
    path('', CommentList.as_view()),
    path('<int:pk>/', CommentDetails.as_view()),
]