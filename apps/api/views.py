from django.shortcuts import render

from rest_framework import generics

from apps.posts.models import Post
from apps.posts import serializers

# Create your views here.

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.order_by('-dateCreate')
    serializer_class = serializers.PostSerializer
