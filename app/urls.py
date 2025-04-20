from django.contrib import admin
from django.urls import path,include

from app.views import PostListAPIView, PostAPIView

urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostAPIView.as_view(), name='post-detail'),
]