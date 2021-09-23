from django.db import models

# Create your models here.

class Blog(models.Model):
    blog_name = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)
    created_date =models.DateTimeField(auto_now=True)