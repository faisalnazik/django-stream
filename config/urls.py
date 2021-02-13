from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('blog.urls')),
    path('', include('tvshows.urls')),
    path('', include('home.urls')),
    path('', include('streams.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    url(r'', include('web.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns
