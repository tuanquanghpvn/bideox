from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^$', views.PostListView.as_view(), name='index'),
   url(r'^p/(?P<id>.+)/(?P<slug>[\w-]+)/$', views.PostDetailView.as_view(),
                                                            name="detail"),
]
