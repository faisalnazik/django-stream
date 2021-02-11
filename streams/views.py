from django.shortcuts import render

# Create your views here.
from .models import TvShowsClassifier, Season, Episode
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Avg, Count, Q, F
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib.postgres.search import TrigramSimilarity
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.views.generic import RedirectView, ListView




class TvShowsClassifierView(ListView):
    model = TvShowsClassifier
    template_name = 'streams/list.html'


def tv_show_list(request):
    object_list = TvShowsClassifier.published.all()
    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')
    try:
        content = paginator.page(page)
    except PageNotAnInteger:
        content = paginator.page(1)
    except EmptyPage:
        content = paginator.page(paginator.num_pages)

    return render(
                'streams/list.html',
                {'page' : page,
                'content' : content,
                }
    )