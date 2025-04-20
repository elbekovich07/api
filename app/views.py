from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import *
from app.serializers import PostModelSerializer


# Create your views here.

class PostListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostModelSerializer(posts, many=True)
        return Response(serializer.data)


class PostAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk is None:
            posts = Post.objects.all()
            serializer = PostModelSerializer(posts, many=True)
            return Response(serializer.data)
        else:
            try:
                post = Post.objects.get(pk=pk)
            except Post.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = PostModelSerializer(post)
            return Response(serializer.data)

    def post(self, request, pk=None):
        serializer = PostModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PostModelSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
