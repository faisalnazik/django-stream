from django.db import models

# Create your models here.
from django.utils import timezone
# from django.contrib.auth.models import CustomUser
from django.urls import reverse
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from mptt.models import MPTTModel, TreeForeignKey
#django mptt for trees 
from django.utils.safestring import mark_safe
from django.db.models import Avg, Count
from ckeditor.fields import RichTextField

class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager,
			self).get_queryset().filter(status='published')




class Post(models.Model):
	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
)
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250,
		unique_for_date='publish')
	author = models.ForeignKey(settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		related_name='blog_posts')
	cover = models.ImageField(upload_to='upload/', null=True)
	body = models.TextField()
	link = models.CharField(max_length=1000, null=True)
	imdb_rating = models.DecimalField(null=True, max_digits=12, decimal_places=1)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	views = models.IntegerField(default=0)
	hearts = models.IntegerField(default=0)
	# categories = models.ManyToManyField('Category', related_name='posts')
	# like     = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="likes")
	status = models.CharField(max_length=10,
		choices=STATUS_CHOICES,
		default='draft')

	class Meta:
		ordering = ('-publish',)
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:post_detail',

						args=[self.publish.year,
						self.publish.month,
						self.publish.day, self.slug])

	def get_api_like_url(self):
		return reverse("blog:like_api", kwargs={"slug": self.slug})

	objects = models.Manager() # The default manager.	
	published = PublishedManager() # Our custom manager.
	tags = TaggableManager()


class Comment(models.Model):
	post = models.ForeignKey(Post,
							on_delete=models.CASCADE,
							related_name='comments')
	name = models.CharField(max_length=80)
	email = models.EmailField()
	body = models.TextField(max_length=300)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)
	
	class Meta:
		ordering = ('created',)

	def __str__(self):
		return f'Comment by {self.name} on {self.post}'


'''


class Category(MPTTModel):
    STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
)
    parent = TreeForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image=models.ImageField(blank=True,upload_to='images/')
    status=models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    slug = models.SlugField(null=False, unique=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.title]                  # post.  use __unicode__ in place of
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])


class Product(models.Model):
    STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
)

    
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #many to one relation with Category
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    detail=RichTextUploadingField()
    image=models.ImageField(upload_to='images/',null=False)
    imdb_rating = models.DecimalField(null=True, max_digits=12, decimal_places=1)
    slug = models.SlugField(null=False, unique=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    link = models.CharField(max_length=1000, null=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES, default='draft')
    def __str__(self):
        return self.title


    ## method to create a fake table field in read only mode
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

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


class Images(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title


class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True,max_length=100)
    phone = models.CharField(blank=True,max_length=15)
    fax = models.CharField(blank=True,max_length=15)
    email = models.CharField(blank=True,max_length=50)
    smtpserver = models.CharField(blank=True,max_length=50)
    smtpemail = models.CharField(blank=True,max_length=50)
    smtppassword = models.CharField(blank=True,max_length=10)
    smtpport = models.CharField(blank=True,max_length=5)
    icon = models.ImageField(blank=True,upload_to='images/')
    facebook = models.CharField(blank=True,max_length=50)
    instagram = models.CharField(blank=True,max_length=50)
    twitter = models.CharField(blank=True,max_length=50)
    youtube = models.CharField(blank=True, max_length=50)
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status=models.CharField(max_length=10,choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

'''

