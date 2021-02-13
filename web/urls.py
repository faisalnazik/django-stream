from django.conf.urls import url
from web import views, api

urlpatterns = [
    url(r'^main/$', views.home, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^data/(?P<movie_slug>\D+)/$', views.movie, name='movie'),
    url(r'^categories/(?P<category_slug>\D+)/$', views.category, name='categoria'),
    url(r'^pesquisa/(?P<keyword>\D+)/$', views.search, name='pesquisa'),
    url(r'^adicionalista$', api.addToList, name='adicionalista'),
    url(r'^dologin/$', api.doLogin, name='do_login'),
    url(r'^doregister/$', api.doRegister, name='do_register'),
]