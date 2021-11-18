from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse

class User(AbstractUser):
    avatar=models.ImageField(upload_to='users/', height_field=None, width_field=None, max_length=512)

    def __str__(self):
        return self.username

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    thumbnail=models.ImageField(upload_to='posts/', height_field=None, width_field=None, max_length=512)
    publish_date=models.DateTimeField(auto_now_add=True)
    last_updated=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    slug=models.SlugField()

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    def get_like_url(self):
        return reverse("like", kwargs={"slug": self.slug})


    @property
    def get_comment_count(self):
        return self.comment_set.all().count()

    @property
    def get_like_count(self):
        return self.like_set.all().count()

    @property
    def get_view_count(self):
        return self.postview_set.all().count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)   

    def __str__(self):
        return self.user.username

class PostView(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Like(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
