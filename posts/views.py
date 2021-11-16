from django.shortcuts import render

from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView


class PostListView(ListView):
    model=Post
