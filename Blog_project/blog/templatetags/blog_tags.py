from blog.models import Post
from django import template

register = template.Library()


@register.simple_tag
def total_tags():
    return Post.objects.count()


@register.inclusion_tag('blog/latest_posts123.html')
def show_latest_post():
    latest_post = Post.objects.order_by('-publish')[:3]
    return {'latest_post': latest_post}


from django.db.models import Count


# @register.assignment_tag
def get_most_commented_posts(count=5):
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
