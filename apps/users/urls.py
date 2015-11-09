from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^signup/$', views.SignupUserView.as_view(), name='signup'),
    url(r'^login/$', views.LoginUserView.as_view(), name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', 
                        {'next_page': '/'}, name='logout'),
]