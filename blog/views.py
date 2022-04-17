from django.shortcuts import render
from .models import Post
from . forms import PostForm, EditForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#---------------------------------------------------------------------------------------#

class PostList(ListView):
    model = Post
    template_name = 'blog/home.html'

#---------------------------------------------------------------------------------------#

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_details.html'

#---------------------------------------------------------------------------------------#

class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    # fields = '__all__'

#---------------------------------------------------------------------------------------#

class PostUpdate(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/post_update.html'
    # fields = ['title', 'slug', 'content', 'status']

#---------------------------------------------------------------------------------------#

class PostDelete(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home') 
