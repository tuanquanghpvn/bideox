from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='index'),
    url(r'^p/(?P<id>.+)/(?P<slug>.+)/$', views.PostDetailView.as_view(),
                                                            name="detail"),
    url(r'^create/video/$', views.PostCreateView.as_view(),
                                                            name="create"), 
    url(r'^parse/$', views.CheckInfoYoutubeView.as_view(),
                                                            name="parse"),
]
