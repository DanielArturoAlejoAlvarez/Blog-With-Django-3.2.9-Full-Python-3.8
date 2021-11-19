from django import forms
from django.forms.widgets import Textarea
from .models import Comment, Post 

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('__all__')

class CommentForm(forms.ModelForm):
    content=forms.CharField(widget=Textarea(attrs={
        'rows': 4
    }))
    class Meta:
        model=Comment
        fields=('content',)