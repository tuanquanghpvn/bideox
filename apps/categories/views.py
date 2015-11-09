from django.shortcuts import render
from django.views.generic import (DetailView, ListView)

from apps.core.views import BaseView
from apps.categories.models import Category
from apps.posts.models import Post

class CategoryListView(BaseView, ListView):
    model = Post
    template_name = 'categories/index.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': Category.objects.get(id=self.kwargs['pk']).name
            }
        }
        context.update(info)
        return context

    def get_queryset(self):
        slug = self.kwargs.get('slug', None)
        return Post.objects.filter(category__slug=slug).order_by('-dateCreate')

