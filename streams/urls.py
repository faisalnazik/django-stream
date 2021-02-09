from django.urls import path
from . import views
from django.conf.urls import url, include
from django.contrib import admin


app_name = 'streams'

urlpatterns = [

    path('content', views.tv_show_list, name='tv_show_list'),

]