from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^login/', views.LoginView.as_view(), name='login'),

    url(r'^category/$', views.CategoryListView.as_view(), 
                                                    name='category_list'),
    url(r'^category/create/$', views.CategoryCreateView.as_view(),
                                                name='category_create'),
    url(r'^category/update/(?P<pk>[0-9]+)/$',
                                        views.CategoryUpdateView.as_view(),
                                                name='category_update'),
    url(r'^category/delete/(?P<pk>[0-9]+)/$',
                                        views.CategoryDeleteView.as_view(), 
                                                name='category_delete'),

    url(r'^post/$', views.PostListView.as_view(), name='post_list'),
    url(r'^post/create/$', views.PostCreateView.as_view(),
                                            name='post_create'),
    url(r'^post/update/(?P<pk>.+)/$', views.PostUpdateView.as_view(),
                                            name='post_update'),
    url(r'^post/delete/(?P<pk>.+)/$', views.PostDeleteView.as_view(),
                                            name='post_delete'),
]
