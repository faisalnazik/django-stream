from django.urls import path
from streams.views import TvShowsClassifierView
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

app_name = 'streams'

urlpatterns = [

    #path('content/', TemplateView.as_view(template_name="streams/list.html")), 
    path('content/', TvShowsClassifierView.as_view()),
]