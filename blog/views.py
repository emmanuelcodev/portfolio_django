from django.shortcuts import render, get_object_or_404
import os
from .models import BlogPost


# Create your views here.
def allblogs(request):
    blog_post = BlogPost.objects
    return render(request, os.path.join('blogs', 'allblogs.html'), {'blog_post':blog_post})

def detail(request, blog_id):
    detailblog = get_object_or_404(BlogPost, pk=blog_id)
    return render(request, os.path.join('blogs', 'detail.html'), {'blog':detailblog})
