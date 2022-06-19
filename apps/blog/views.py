from django.db import reset_queries
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django.urls import reverse
from django.views import generic

from blog.models import Post

#CARREGA AS PÁGINAS PRINCIPAIS

def carrega_posts(request):
    posts = Post.objects.all()
    return render(request,'blog/posts.html',{'posts':posts })

# Create your views here.
