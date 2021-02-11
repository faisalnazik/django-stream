from django.urls import path
from streams.views import TvShowsClassifierView
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from . import views

from .views import (
        TvShowsListView, 
        TvShowsDetailSlugView
)

app_name = 'streams'

urlpatterns = [

    #path('content/', TemplateView.as_view(template_name="streams/list.html")), 
    path('content/', TvShowsClassifierView.as_view()),
    # path('content2/', views.tv_show_list, name='tv_show_list'),
    # path('content-detail/', views.tv_show_detail, name='tv_show_list'),
    # path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.tv_show_detail, name='tv_show_detail'),
    # path('content2/', TvShowsListView.as_view(), name='tv_show_list'),
    # url(r'^(?P<slug>[\w-]+)/$', TvShowsDetailSlugView.as_view(), name='tv_show_detail'),
]