from django.shortcuts import render

# Create your views here.
import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Avg, Count, Q, F
from django.db.models.functions import Concat
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.template.loader import render_to_string
from django.urls import reverse
from home.forms import SearchForm
from home.models import Setting, ContactForm, ContactMessage, Genre
from config import settings
from tvshows.models import TvShowsClassifier, Episode, Comment
from django.views.generic import ListView, DetailView, View


def TvShowFeaturedListView(request):
	return render(request, "index.html", {'genres': TvShowFeaturedListView.objects.all()})
# class TvShowFeaturedListView(ListView):
#     template_name = "index.html"

#     def get_queryset(self, *args, **kwargs):
#         request = self.request
#         return TvShowsClassifier.objects.all()


# def index(request):

# 	# setting = Setting.objects.get(pk=1)
# 	tv_show_latest = TvShowsClassifier.objects.all().order_by('-id')[:4]
# 	tv_show_slider = TvShowsClassifier.objects.all().order_by('id')[:4]
# 	tv_show_picked = TvShowsClassifier.objects.all().order_by('?')[:4]

# 	page="home"
# 	context={'page':page,
# 			'tv_show_slider': tv_show_slider,
# 			'tv_show_latest': tv_show_latest,
# 			'tv_show_picked': tv_show_picked,
# 			#'category':category
# 			}
# 	return render(request,'index.html',context)
def show_genres(request):
    return render(request, "genres.html", {'genres': Genre.objects.all()})

def TvShowsClassifierView(request):
    return render(request, "TvShowsClassifierView.html", {'TvShowsClassifierView': TvShowsClassifier.objects.all()})