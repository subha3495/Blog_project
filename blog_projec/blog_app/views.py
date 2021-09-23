from django.shortcuts import render,HttpResponse
from .models import Blog
# Create your views here.

def blog_post(request):
    context = {'b':Blog.objects.all()}
    return render(request,'home.html',context )
