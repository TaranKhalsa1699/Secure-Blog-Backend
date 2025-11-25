from django.urls import path
from .views import PostListCreate, PostDetail, CommentListCreate

urlpatterns = [
    path("posts/", PostListCreate.as_view(), name='posts'),
    path("posts/<int:pk>/", PostDetail.as_view(), name='post-detail'),
    path('comments/', CommentListCreate.as_view(), name='comments'),
]