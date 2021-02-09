from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Post


class LatestPostsFeed(Feed):
	title = 'Latest Movies'
	link = reverse_lazy('blog:post_list')
	description = 'New Movies On The Site.'

	def items(self):
		return Post.published.all()[:5]
	
	def item_title(self, item):
		return item.title, item.link

	def item_description(self, item):
		return truncatewords(item.body, 30)