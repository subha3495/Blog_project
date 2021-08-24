from django.contrib import admin
from blog.models import Post,Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','body','publish','created','updated','status']
    prepopulated_fields = {'slug':('title',)}
    list_filter = ('status','author','publish','created')
    search_fields = ('title','body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post','name','email','body','created','updated','active']
    search_fields = ('name','body','email')
    list_filter = ('created','updated','active')


admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)