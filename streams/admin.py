from django.contrib import admin, messages
from django.utils.translation import ngettext
# Register your models here.
from streams.models import TvShowsClassifier, Season, Episode


def make_published(modeladmin, request, queryset):
    queryset.update(status='published')
make_published.short_description = "Mark selected entries as published"
class SeasonInline(admin.TabularInline):
    model = Season

class EpisodeInline(admin.TabularInline):
    model = Episode

class TvShowsClassifierAdmin(admin.ModelAdmin):
    list_display = ['title','starring', 'description', 'imdb_rating', 'slug','views', 'status']
    ordering = ['create_at','title']
    actions = [make_published]
    empty_value_display = '-empty-'
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        SeasonInline,
        
    ]

class SeasonAdmin(admin.ModelAdmin):
    list_display = ['season_parent', 'title', 'slug', 'status']
    ordering = ['create_at','title']
    actions = [make_published]
    empty_value_display = '-empty-'
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        
        EpisodeInline,
    ]
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ['episode_of', 'title', 'description', 'slug','views','link', 'status']
    ordering = ['create_at','title']
    actions = [make_published]
    empty_value_display = '-empty-'
    prepopulated_fields = {"slug": ("title",)}
    



admin.site.register(TvShowsClassifier,TvShowsClassifierAdmin)
admin.site.register(Season,SeasonAdmin)
admin.site.register(Episode,EpisodeAdmin)