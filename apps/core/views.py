from django.shortcuts import render
from django.views.generic.base import ContextMixin

from apps.categories.models import Category
from apps.posts.models import Post

class BaseView(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['most_popular'] = Post.objects.order_by('-dateCreate').exclude(externalView__lt=20000)[0:6]
        return context 

