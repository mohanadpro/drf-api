from django.urls import path
from .views import LikeList, LikeDetails
urlpatterns = [
    path('', LikeList.as_view()),
    path('<int:pk>/', LikeDetails.as_view()),
]