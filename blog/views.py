from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.shortcuts import render, get_object_or_404
import markdown

# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={
                                'title': 'Bymost',
                                'description': 'Beyond The Most',
                                'post_list' : post_list
                                })

def detail(request, category, title):
    post = get_object_or_404(Post, title = title)
    return render(request, 'blog/single.html', context = {'post' : post})

def category(request, category):
    return render(request, 'blog/about_me.html')

def about_me(request):
    return render(request, 'blog/about_me.html')
