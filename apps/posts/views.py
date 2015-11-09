from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView)

from apps.core.views import BaseView, LoginRequiredMixin
from apps.posts.models import Post
from apps.categories.models import Category

class PostListView(BaseView, ListView):
    template_name = 'posts/index.html'
    model = Post
    paginate_by = 15 

    def get_queryset(self):
        return Post.objects.order_by('-dateCreate')

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

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('id', 'name', 'slug', 'description', 'videoDurationFe', 
                'externalView', 'category',)
    template_name = 'posts/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Submit video - Bideox'
            }
        }
        context['category'] = Category.objects.all()
        context.update(info)
        return context

    def get_success_url(self):
        return reverse_lazy('posts:create')