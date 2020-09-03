from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, DeleteView
from . models import Post
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'blog_master/home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_master/post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog_master/post_new.html'
    fields = ['titulo', 'autor','conteudo']
    success_url = reverse_lazy('home')
    # fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog_master/post_edit.html'
    fields = ['titulo','conteudo']
    # fields = '__all__'

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog_master/post_delete.html'
    success_url = reverse_lazy('home')
    # fields = '__all__'
