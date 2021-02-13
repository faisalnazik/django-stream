from __future__ import unicode_literals

from django.contrib import admin
from . models import Category, Movie, Block, Actor, MovieDetail, WishList

# Register your models here.
admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Block)
admin.site.register(Actor)
admin.site.register(MovieDetail)
admin.site.register(WishList)