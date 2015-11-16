from django.shortcuts import render

from rest_framework import generics

from apps.posts.models import Post
from apps.posts import serializers

# Create your views here.

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.order_by('-dateCreate')
    serializer_class = serializers.PostSerializer

class CategoryListAPIView(generics.ListAPIView):
    serializer_class = serializers.PostSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Post.objects.filter(category__slug=slug)\
                .order_by('-dateCreate')

