from django.shortcuts import render
from django.views import generic
from . models import Post


# Create your views here.

NUMBER_RECENT_POSTS = 3


class HomeView(generic.ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = '-created_at'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_post'] = Post.objects.all().order_by('-created_at')[:NUMBER_RECENT_POSTS]
        return context


class BlogListView(generic.ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = '-created_at'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(category__name='Blog')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_post'] = Post.objects.all().order_by('-created_at')[:NUMBER_RECENT_POSTS]
        return context


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_post'] = Post.objects.all().order_by('-created_at')[:NUMBER_RECENT_POSTS]
        return context


class PostCreateView(generic.CreateView):
    model = Post
    fields = ('author', 'title', 'description', 'category', 'tags', 'featured_image',)
    template_name = 'blog/create_post.html'


class PostUpdateView(generic.UpdateView):
    model = Post
    fields = ('author', 'title', 'description', 'category', 'tags', 'featured_image',)
    template_name = 'blog/create_post.html'




