from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from apps.posts.models import Post
from apps.posts.serializers import PostSerializer

# Create your views here.

class PostAPIViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,) # тапл, разрешение 

