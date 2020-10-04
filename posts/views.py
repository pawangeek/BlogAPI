from django.shortcuts import render
from rest_framework import generics, permissions

from .permissions import IsAuthorOnly
from .models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOnly,  permissions.IsAuthenticated)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# permissions.IsAuthenticated to limit view level permissions
# Only user with account able to see the api, else people see a forbidden status
