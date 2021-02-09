# from django.db import models
# from django.utils import timezone
# from django.urls import reverse
# from django.conf import settings
# from ckeditor_uploader.fields import RichTextUploadingField
# from taggit.managers import TaggableManager
# from mptt.models import MPTTModel, TreeForeignKey
# from django.utils.safestring import mark_safe
# from django.db.models import Avg, Count
# from ckeditor.fields import RichTextField
# from django.forms import ModelForm




# class TvShowsClassifier(models.Model): 
#     STATUS_CHOICES = (
# 		('draft', 'Draft'),
# 		('published', 'Published'),
# 	)
    
#     title = models.CharField(max_length=50)
#     starring = models.CharField(max_length=255)
#     description = models.TextField()
#     imdb_rating = models.DecimalField(null=True, max_digits=12, decimal_places=1)
#     slug = models.SlugField(null=False, unique=True)
#     views = models.IntegerField(default=0)
#     create_at=models.DateTimeField(auto_now_add=True)
#     update_at=models.DateTimeField(auto_now=True)
#     status=models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

#     def __str__(self):
#         return self.title

#     class MPTTMeta:
#         order_insertion_by = ['title']

#     def get_absolute_url(self):
#         return reverse('tvshow_detail', kwargs={'slug': self.slug})

#     def __str__(self):                           
#         full_path = [self.title]                  
#         k = self.parent
#         while k is not None:
#             full_path.append(k.title)
#             k = k.parent
#         return ' / '.join(full_path[::-1])


# class Season(models.Model):
# 	season_parent = models.ForeignKey(TvShowsClassifier, on_delete=models.CASCADE)
# 	title = models.CharField(max_length=150)
# 	slug = models.SlugField(null=False, unique=True)
# 	create_at= models.DateTimeField(auto_now_add=True)
# 	update_at= models.DateTimeField(auto_now=True)
# 	status = models.CharField(max_length=10,choices=STATUS_CHOICES, default='draft')

#     def __str__(self):
#         return self.title


# class Episode(models.Model):
#     STATUS_CHOICES = (
# 		('draft', 'Draft'),
# 		('published', 'Published'),
# 	)
#     episode_parent = models.ForeignKey(Season, on_delete=models.CASCADE)
#     title = models.CharField(max_length=150)
#     description = models.TextField()
#     image=models.ImageField(upload_to='images/',null=False)
#     slug = models.SlugField(null=False, unique=True)
#     create_at=models.DateTimeField(auto_now_add=True)
#     update_at=models.DateTimeField(auto_now=True)
#     views = models.IntegerField(default=0)
#     link = models.CharField(max_length=1000, null=True)
#     status=models.CharField(max_length=10,choices=STATUS_CHOICES, default='draft')

#     def __str__(self):
#         return self.title


#     def get_absolute_url(self):
#         return reverse('episode_detail', kwargs={'slug': self.slug})

#     