from django.urls import path, include, re_path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    re_path(r'^post/new/$', views.post_new, name='post_new'),
    re_path(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^login/$',  LoginView.as_view(template_name='blog/login.html'), name="login"),
    re_path(r'^logout/$', views.logout_session, name='logout'),
    re_path(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    re_path(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    re_path(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
]
