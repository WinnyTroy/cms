from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Post


def index(request):

    posts = Post.objects.order_by('-created_at')[:6]
    template = loader.get_template('theblog/blogpage.html')
    context = {
        'title': 'Blog',
        'posts': posts
    }
    return HttpResponse(template.render(context, request))


def show(request, id):
    post = Post.objects.filter(id=id)[0]
    template = loader.get_template('theblog/show.html')
    context = {
        'title': post.title,
        'post': post
    }
    return HttpResponse(template.render(context, request))
