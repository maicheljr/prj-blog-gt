from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, DeleteView
from . models import Post
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import PostForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'blog_master/home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_master/post_detail.html'


class BlogCreateView(SuccessMessageMixin,CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('home')
    template_name = 'blog_master/post_new.html'
    success_message = "%(field)s - Criado com sucesso!"
    # fields = ['titulo','conteudo']

    def form_valid(self, form):
        object = form.save(commit=False)
        object.autor = self.request.user
        object.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo
        )

class BlogUpdateView(LoginRequiredMixin,SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('home')
    template_name = 'blog_master/post_edit.html'
    # fields = ['titulo','conteudo']
    success_message = "%(field)s - Alterado com sucesso!"

    def form_valid(self, form):
        object = form.save(commit=False)
        object.autor = self.request.user
        object.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )



class BlogDeleteView(SuccessMessageMixin,DeleteView):
    model = Post
    template_name = 'blog_master/post_delete.html'
    success_url = reverse_lazy('home')
    # fields = '__all__'
    success_message = "Deletado com sucesso!!!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(BlogDeleteView,self).delete(request, *args, **kwargs)