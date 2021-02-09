from django.shortcuts import render

# Create your views here.
from .models import TvShowsClassifier, Season, Episode
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Avg, Count, Q, F
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib.postgres.search import TrigramSimilarity
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.views.generic import RedirectView



def tv_show_list(request, tag_slug=None):
    object_list = TvShowsClassifier.published.all()
    # if tag_slug:
    #     tag = get_object_or_404(Tag, slug=tag_slug)
    #     object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list, 6) # 6 posts in each page
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request,
                'streams/list.html',
                {'page': page,
                'posts': posts,})
                #'tag' 	: tag,
                #'link' : link