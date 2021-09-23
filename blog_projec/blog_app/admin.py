from django.contrib import admin
from .models import Blog
# Register your models here.
class Blog_Admin(admin.ModelAdmin):
    list_display = ['blog_name','author_name','created_date']

admin.site.register(Blog,Blog_Admin)