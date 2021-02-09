from django.urls import path
from . import views
from .feeds import LatestPostsFeed
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from django.contrib import admin

app_name = 'blog'


urlpatterns = [
# post views
	path('', views.post_list, name='post_list'),
	path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
	path('<int:post_id>/share/', views.post_share, name='post_share'),
	path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
	path('feed/', LatestPostsFeed(), name='post_feed'),
	path('search/', views.post_search, name='post_search'),
	# path('index', views.index, name='index'),

]
