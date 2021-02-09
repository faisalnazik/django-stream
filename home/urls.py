from django.urls import path
from django.conf.urls import url
from . import views
from .views import (
	show_genres,
	TvShowsClassifierView
	)

urlpatterns = [
    path('index2/', views.show_genres, name='index'),
    path('classifier/', views.TvShowsClassifierView, name='index'),
    # url(r'^genres/$', show_genres.as_view(), name='list'),
]