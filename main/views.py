from django.shortcuts import render
from .models import Category, Post


# Create your views here.
def home(requests):
    category = Category.objects.all()
    posts = Post.objects.all()
    return render(requests, 'home.html', context={"category": category, "posts":posts})

def post_page(request, category ,slug):
    return render(request, 'post.html')

def category_page(request, slug):
    return render(request, 'category.html')