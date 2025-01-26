from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
# Create your views here.
def BlogView(request):
    return render(request,"blog.html")

class Blogview(TemplateView):
    template_name='blog/blog.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["name"] = "mohsen"
        context["posts"] = Post.objects.all()
        return context

class PostList(ListView):
    # model = Post
    queryset = Post.objects.filter(status=True)
    ordering = "-id"
    paginate_by = '2'
    context_object_name = 'posts'
    
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts
    
    