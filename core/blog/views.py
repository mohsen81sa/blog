from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post
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