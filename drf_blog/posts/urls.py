from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('api/posts/', PostList.as_view()),
    path('api/posts/<int:pk>/', PostDetail.as_view()),
]
