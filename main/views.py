from django.shortcuts import render
from .models import Category, Post


# Create your views here.
def home(requests):
    category = Category.objects.all()
    posts = Post.objects.all()
    return render(requests, 'index.html', context={"category": category, "posts":posts})

def post_page(request, date_added, post_slug):
    post = Post.objects.get(post_slug=post_slug)
    return render(request, 'post.html', context={"post":post})

def category_page(request, category_slug):
    return render(request, 'category.html')