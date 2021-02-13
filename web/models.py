from __future__ import unicode_literals
from django.db import models
from django.conf import settings
# Create your models here.

from django.contrib.auth.models import User

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    slug = models.CharField(max_length=300)

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    slug = models.CharField(max_length=300)
    url = models.CharField(max_length=300)
    videoUrl = models.CharField(max_length=300)
    categories = models.ManyToManyField(Category)

class Block(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    order = models.IntegerField()
    movies = models.ManyToManyField(Movie)

class Actor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)

class MovieDetail(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=300)
    rating = models.DecimalField(decimal_places=2, max_digits=8)
    year = models.IntegerField()
    age = models.IntegerField()
    duration = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie,db_column="movie_id", null=False, on_delete=models.CASCADE)
    casting = models.ManyToManyField(Actor)

class WishList(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,db_column="user_id", null=False , on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,db_column="movie_id", null=False, on_delete=models.CASCADE)
    active = models.IntegerField(default=1)