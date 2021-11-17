from django.shortcuts import render

from .models import Post,Comment,PostView,Like
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import PostForm

class PostListView(ListView):
    model=Post

class PostDetailView(DetailView):
    model=Post

class PostCreateView(CreateView):
    form_class=PostForm
    model=Post 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'create'
        }) 
        return context
    

    # fields=(
    #     'title',
    #     'content',
    #     'thumbnail',
    #     'author',
    #     'slug'
    # )

class PostUpdateView(UpdateView):
    form_class=PostForm
    model=Post 

    # fields=(
    #     'title',
    #     'content',
    #     'thumbnail',
    #     'author',
    #     'slug'
    # )

class PostDeleteView(DeleteView):
    model=Post
    success_url='/'