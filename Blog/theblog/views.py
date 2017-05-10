from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse
from urllib import quote_plus
from django.template import loader

from .models import Post


def index(request):

    posts = Post.objects.order_by('-created_at')[:6]
    paginator = Paginator(posts, 3)  # Show 2 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    template = loader.get_template('theblog/blogpage.html')
    context = {
        'title': 'Blog',
        'posts': posts,
        'page_request_var': page_request_var,
    }
    return HttpResponse(template.render(context, request))


def show(request, slug):
    post = Post.objects.filter(slug=slug)[0]
    share_string = quote_plus(post.body)
    template = loader.get_template('theblog/show.html')
    context = {
        'title': post.title,
        'post': post,
        'share_string': share_string
    }
    return HttpResponse(template.render(context, request))

