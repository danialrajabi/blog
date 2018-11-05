from django.shortcuts import render
from django.views import generic
from . models import Post


# Create your views here.


class HomeView(generic.ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = '-created_at'