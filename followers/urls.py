from django.urls  import path
from .views import FollowList, FollowDetails
urlpatterns = [
    path('', FollowList.as_view()),
    path('<int:pk>', FollowDetails.as_view())
]