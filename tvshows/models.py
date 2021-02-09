from django.db import models
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


class TvShowsClassifier(MPTTModel): 
    STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
	)
    parent = TreeForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    starring = models.CharField(max_length=255)
    description = RichTextUploadingField()
    imdb_rating = models.DecimalField(null=True, max_digits=12, decimal_places=1)
    slug = models.SlugField(null=False, unique=True)
    views = models.IntegerField(default=0)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('tvshow_detail', kwargs={'slug': self.slug})

    def __str__(self):                           
        full_path = [self.title]                  
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])

class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    tvshow =models.ForeignKey(TvShowsClassifier, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.CharField(max_length=250,blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status=models.CharField(max_length=10,choices=STATUS, default='New')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('create_at',)   
    def __str__(self):
        return self.subject

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']


class Episode(models.Model):
    STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
	)
    episode_parent = models.ForeignKey(TvShowsClassifier, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = RichTextUploadingField()
    image=models.ImageField(upload_to='images/',null=False)
    slug = models.SlugField(null=False, unique=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    link = models.CharField(max_length=1000, null=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title


    # method to create a fake table field in read only mode
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    def get_absolute_url(self):
        return reverse('episode_detail', kwargs={'slug': self.slug})

    def avaregereview(self):
        reviews = Comment.objects.filter(product=self, status='True').aggregate(avarage=Avg('rate'))
        avg=0
        if reviews["avarage"] is not None:
            avg=float(reviews["avarage"])
        return avg

    def countreview(self):
        reviews = Comment.objects.filter(product=self, status='True').aggregate(count=Count('id'))
        cnt=0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt


# class Images(models.Model):
#     parent =models.ForeignKey(TvShowsClassifier, on_delete=models.CASCADE)
#     title = models.CharField(max_length=150)
#     image = models.ImageField(blank=True, upload_to='images/')

#     def __str__(self):
#         return self.parent
