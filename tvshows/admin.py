from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import TvShowsClassifier, Comment, CommentForm, Episode
import admin_thumbnails

# @admin_thumbnails.thumbnail('image')
# class EpisodeImageInline(admin.TabularInline):
#     model = Images
#     readonly_fields = ('id',)
#     extra = 1

class TvShowsClassifierAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_episodes_count', 'related_episodes_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}
    # inlines = [EpisodeImageInline]
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = TvShowsClassifier.objects.add_related_count(
                qs,
                Episode,
                'episode_parent',
                'episodes_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = TvShowsClassifier.objects.add_related_count(qs,
                 Episode,
                 'episode_parent',
                 'episodes_count',
                 cumulative=False)
        return qs

    def related_episodes_count(self, instance):
        return instance.episodes_count
    related_episodes_count.short_description = 'Related episodes (for this specific episode_parent)'

    def related_episodes_cumulative_count(self, instance):
        return instance.episodes_cumulative_count
    related_episodes_cumulative_count.short_description = 'Related episodes (in tree)'





# @admin_thumbnails.thumbnail('image')
# class ImagesAdmin(admin.ModelAdmin):
#     list_display = ['image','title','image_thumbnail']

class EpisodeAdmin(admin.ModelAdmin):
    list_display = ['title','episode_parent', 'status','image_tag']
    list_filter = ['episode_parent']
    readonly_fields = ('image_tag',)
    # inlines = [EpisodeImageInline]
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
	list_display = ['subject','comment', 'status','create_at']
	list_filter = ['status']
	readonly_fields = ('subject','comment','ip','user','tvshow','rate','id')



admin.site.register(TvShowsClassifier,TvShowsClassifierAdmin)
admin.site.register(Episode,EpisodeAdmin)
admin.site.register(Comment,CommentAdmin)
# admin.site.register(Images,ImagesAdmin)