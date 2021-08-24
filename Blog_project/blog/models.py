from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.
from django.urls import reverse

class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (('dfaft','Dfaft'),('published','Published'))
    title          = models.CharField(max_length=50)
    slug           = models.SlugField(max_length=200,unique_for_date='publish')
    author         = models.ForeignKey(User,related_name='blog_posts',on_delete=models.CASCADE)
    body           = models.TextField()
    publish        = models.DateTimeField(auto_now =True)
    created        = models.DateTimeField(auto_now =True)
    updated        = models.DateTimeField(auto_now =True)
    status         = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    objects        = CustomManager()
    tags           = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])

class Comment(models.Model):
    post  = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE )
    name  = models.CharField(max_length=50)
    email = models.EmailField()
    body  = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    active  = models.BooleanField(default=True)
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Commented by {} on {}'.format(self.name,self.post)

