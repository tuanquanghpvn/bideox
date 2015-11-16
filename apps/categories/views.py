from django.shortcuts import render
from django.views.generic import (TemplateView)

from apps.core.views import BaseView
from apps.categories.models import Category

class CategoryListView(BaseView, TemplateView):
    template_name = 'categories/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': Category.objects.get(id=self.kwargs['pk']).name
            }
        }
        context['slug']= self.kwargs['slug']
        context.update(info)
        return context