from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm, CommentForm, SearchForm
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count, Avg, Count, Q, F
from django.db.models.functions import Concat
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib.postgres.search import TrigramSimilarity
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from django.http import JsonResponse
# from django.conf import settings
import json
from config import settings
from django.contrib import messages
from django.template.loader import render_to_string




def post_share(request, post_id):
	# Retrieve post by id
	post = get_object_or_404(Post, id=post_id, status='published')
	sent = False 
	
	if request.method == 'POST':
		# Form was submitted
		form = EmailPostForm(request.POST)
		if form.is_valid():
			# Form fields passed validation
			cd = form.cleaned_data
			# ... send email
			post_url = request.build_absolute_uri(post.get_absolute_url())
			subject = f"{cd['name']} recommends you watch this movie "f"{post.title}"
			message = f"Read {post.title} at {post_url}\n\n" f"{cd['name']}\'s comments: {cd['comments']}" 
			send_mail(subject, message, 'sualehbasit@gmail.com',[cd['to']])
			sent = True
	else:
		form = EmailPostForm()
	return render(request, 'blog/share.html',{'post': post,
														'form': form,
														'sent' : sent})



def post_list(request, tag_slug=None):
	object_list = Post.published.all()
	tag = None
	if tag_slug:
		tag = get_object_or_404(Tag, slug=tag_slug)
		object_list = object_list.filter(tags__in=[tag])

	paginator = Paginator(object_list, 6) # 3 posts in each page
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
				'blog/list.html',
				{'page': page,
				'posts': posts,
				'tag' 	: tag,})
				#'link' : link





def post_detail(request, year, month, day, post):


	post = get_object_or_404(Post, slug=post,
						status='published',
						publish__year=year,
						publish__month=month,
						publish__day=day)
	# List of similar posts

	post_tags_ids = post.tags.values_list('id', flat=True)
	similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
	similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]

	# post hit counts
	post.views 	=  post.views + 1
	post.save()

	# List of active comments for this post
	comments = post.comments.filter(active=True)
	new_comment = None
	if request.method == 'POST':
		# A comment was posted
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			# Create Comment object but don't save to database yet
			new_comment = comment_form.save(commit=False)
			# Assign the current post to the comment
			new_comment.post = post
			# Save the comment to the database
			new_comment.save()
			comment_form.is_valid()

	else:
		comment_form = CommentForm()
	return render(request,
				'blog/detail.html',
				{'post': post,
					'comments': comments,
					'new_comment': new_comment,
					'comment_form': comment_form})

	

	

	return render(request,
					'blog/detail.html',
					{'post': post,
					#'link' : link,
					'comments': comments,
					'new_comment': new_comment,
					'comment_form': comment_form,
					'similar_posts': similar_posts})




'''Post Search '''


def post_search(request):

	form = SearchForm()
	query = None
	results = []

	if 'query' in request.GET:
		form = SearchForm(request.GET)
		if form.is_valid():
			query = form.cleaned_data['query']
			search_vector = SearchVector('title', weight='A') + SearchVector('body', weight='B')
			search_query = SearchQuery(query)

			results = Post.published.annotate(
				similarity=TrigramSimilarity('title', query),
			).filter(similarity__gt=0.1).order_by('-similarity')

			# 	search=search_vector,
			# 	rank=SearchRank(search_vector, search_query)
			# ).filter(rank__gte=0.3).order_by('-rank')
			
	return render(request,
		'blog/search.html',
			{'form': form,
			'query': query,
			'results': results})



