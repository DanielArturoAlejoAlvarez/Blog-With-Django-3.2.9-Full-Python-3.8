from django.shortcuts import render, get_object_or_404, redirect

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


def like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like_qs = Like.objects.filter(user=request.user, post=post)
    if like_qs.exists():
        like_qs[0].delete()
        return redirect('detail', slug=slug)
    Like.objects.create(user=request.user, post=post)
    return redirect('detail', slug=slug)