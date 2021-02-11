from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.safestring import mark_safe
from django.db.models import Avg, Count
from ckeditor.fields import RichTextField
from django.forms import ModelForm


class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager,
			self).get_queryset().filter(status='published')

class TvShowsQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)
    
    def search(self, query):
        lookups = (Q(title__icontains=query) | 
                  Q(description__icontains=query) |
                  Q(slug__icontains=query) |
                  Q(starring__icontains=query)
                  )
        # tshirt, t-shirt, t shirt, red, green, blue,
        return self.filter(lookups).distinct()



class TvShowsManager(models.Manager):
    def get_queryset(self):
        return TvShowsQuerySet(self.model, using=self._db)
    def all(self):
        return self.get_queryset().active()

    def search(self, query):
        return self.get_queryset().active().search(query)

class TvShowsClassifier(models.Model): 
    STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
	)
    
    title = models.CharField(max_length=50)
    starring = models.CharField(max_length=255)
    description = models.TextField()
    imdb_rating = models.DecimalField(null=True, max_digits=12, decimal_places=1)
    slug = models.SlugField(null=False, unique=True)
    views = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-create_at',)

     # Our custom manager.

    # def get_absolute_url(self):
    #     return reverse('streams:tv_show_detail', args=self.slug)
    def get_absolute_url(self):
        return reverse('streams:tv_show_detail', 

                        args=[
                        self.slug])

    objects = models.Manager() # The default manager.	
    published = PublishedManager()
    # objects = TvShowsManager()
    # def get_absolute_url(self):
    #     #return "/products/{slug}/".format(slug=self.slug)
    #     return reverse("streams:tv_show_detail", kwargs={"slug": self.slug})




class Season(models.Model):
    STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
	)
    season_parent = models.ForeignKey(TvShowsClassifier, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug = models.SlugField(null=False, unique=True)
    active = models.BooleanField(default=True)
    create_at= models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title


class Episode(models.Model):
    STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
	)
    episode_of = models.ForeignKey(Season, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField(null=True)
    active = models.BooleanField(default=True)
    image=models.ImageField(upload_to='images/',null=False)
    slug = models.SlugField(null=False, unique=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    link = models.CharField(max_length=1000, null=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title


    

    