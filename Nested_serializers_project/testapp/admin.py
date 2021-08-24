from django.contrib import admin
from testapp.models import Author,Book
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','subject',]

class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author','relese_date','rating']

admin.site.register(Author,AuthorAdmin)

admin.site.register(Book,BookAdmin)