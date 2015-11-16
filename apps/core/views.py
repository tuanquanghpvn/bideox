from django.shortcuts import render
from django.views.generic.base import ContextMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.views.decorators.gzip import gzip_page

from rest_framework.pagination import PageNumberPagination

from apps.categories.models import Category
from apps.posts.models import Post

class BaseView(ContextMixin):
    @method_decorator(gzip_page)
    def dispatch(self, request, *args, **kwargs):
        return super(BaseView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['most_popular'] = Post.objects.order_by('-dateCreate')\
                                        .exclude(externalView__lt=20000)[0:6]
        context['rand'] = Post.objects.order_by('-dateCreate').order_by('?')[0:6]
        return context
    
class AdminRequiredMixin(object):
    @method_decorator(permission_required('is_superuser', login_url='/admin/login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
