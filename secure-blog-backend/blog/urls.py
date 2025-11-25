from django.urls import path
from .views import PostListCreate, PostDetail, CommentListCreate

urlpatterns = [
    path("posts/", PostListCreate.as_view()),
    path("posts/<int:pk>/", PostDetail.as_view()),
    path("comments/", CommentListCreate.as_view()),
]
