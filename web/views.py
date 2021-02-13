from __future__ import unicode_literals
from django.shortcuts import render
from web.datasource import DataSource
from django.http import JsonResponse

ds = DataSource()

def home(request):
    resp = ds.homeData()
    return render(request, 'pages/home.html', resp)

def login(request):
    resp = {}
    return render(request, 'pages/login.html', resp)

def movie(request, movie_slug):
    resp = ds.movieData(movie_slug)
    return render(request, 'pages/movie.html', resp)

def category(request, category_slug):
    resp = ds.categoryData(category_slug)
    return render(request, 'pages/category.html', resp)

def search(request, keyword):
    resp = ds.searchData(keyword)
    return render(request, 'pages/search.html', resp)