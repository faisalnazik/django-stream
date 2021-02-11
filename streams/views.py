from django.shortcuts import render

# Create your views here.
from .models import TvShowsClassifier, Season, Episode
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Avg, Count, Q, F
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib.postgres.search import TrigramSimilarity
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.views.generic import RedirectView, ListView, DetailView
# from analytics.mixins import ObjectViewedMixin



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


def tv_show_detail(request, year, month, day, post):

    post = get_object_or_404(TvShowsClassifierView, slug=post,
                        status='published',
                        publish__year=year,
                        publish__month=month,
                        publish__day=day)

    return render(request, 'streams/detail.html',
                            {'post' : post,
                            })
    


class TvShowsListView(ListView):
    template_name = "streams/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(TvShowsListView, self).get_context_data(*args, **kwargs)
        
        return context
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return TvShowsClassifier.objects.all()


class TvShowsDetailSlugView(DetailView):
    queryset = TvShowsClassifier.objects.all()
    template_name = "streams/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(TvShowsDetailSlugView, self).get_context_data(*args, **kwargs)
        
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = TvShowsClassifier.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product doesn't exist")
        return instance