from django.db import models
from django.contrib.auth.models import AbstractUser

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
