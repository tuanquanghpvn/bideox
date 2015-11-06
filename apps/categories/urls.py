from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^(?P<pk>[0-9]+)-(?P<slug>[\w-]+)/$',
                    views.CategoryListView.as_view(), name='list') 
]

