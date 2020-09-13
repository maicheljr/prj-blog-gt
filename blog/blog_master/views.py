from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, DeleteView
from . models import Post
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib import messages

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'blog_master/home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_master/post_detail.html'


class BlogCreateView(SuccessMessageMixin,CreateView):
    model = Post
    template_name = 'blog_master/post_new.html'
    fields = ['titulo', 'autor','conteudo']
    success_url = reverse_lazy('home')
    success_message = "%(field)s - Foi criado com sucesso!!!"


    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )

class BlogUpdateView(SuccessMessageMixin, UpdateView):
    model = Post
    template_name = 'blog_master/post_edit.html'
    fields = ['titulo','conteudo']



class BlogDeleteView(SuccessMessageMixin,DeleteView):
    model = Post
    template_name = 'blog_master/post_delete.html'
    success_url = reverse_lazy('home')
    # fields = '__all__'
    success_message = "Deletado com sucesso!!!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(BlogDeleteView,self).delete(request, *args, **kwargs)