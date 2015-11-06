from django.shortcuts import render
from django.views.generic import (ListView, DetailView,)

from apps.core.views import BaseView
from apps.posts.models import Post

class PostListView(BaseView, ListView):
    template_name = 'posts/index.html'
    model = Post
    paginate_by = 15 

    def get_queryset(self):
        return Post.objects.order_by('dateCreate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Bideox - Funny bideo'
            }
        }
        context.update(info)
        return context

class PostDetailView(BaseView, DetailView):
    template_name = 'posts/detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': self.object.name
            }
        }
        context.update(info)
        return context
