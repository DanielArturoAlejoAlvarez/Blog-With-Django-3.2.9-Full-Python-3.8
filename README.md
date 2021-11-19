# Blog-With-Django-3.2.9-Full-Python-3.8

## Description

This repository is a Software of Application with Python.

## Virtual

Using pipenv, virtualenv preferably.

## Installation

Using Django, Django Rest Framework preferably.

![alt text](https://1.bp.blogspot.com/-Buv4_R37zXU/X52GkTyp2sI/AAAAAAABRIc/xMjPZef7ETIeW9cw4-7MejW6DGfV_ZkDwCLcBGAsYHQ/w640-h413/October2020-Templates_2.gif)

## DataBase

Using SQLite3, PostgreSQL, MySQL, MongoDB,etc.

## Apps

Using Postman, Insomnia, Talend API Tester,etc.



## Usage

```shell
$ git clone https://github.com/DanielArturoAlejoAlvarez/Blog-With-Django-3.2.9-Full-Python-3.8.git [NAME 
$ source env/bin/activate
$ python manage.py makemigrations
$ pthyon manage.py migrate
$ python manage.py runserver
```

Follow the following steps and you're good to go! Important:

![alt text](https://i.ytimg.com/vi/HWg3zXWwre8/maxresdefault.jpg)

## Coding

### Config

```python
DATABASE_URI='mysql+pymysql://{}:{}@{}/{}'.format(DB_USER,DB_PASSWORD,DB_HOST,DB_NAME)
```

### Routes

```python
from posts.views import (
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
    like
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', PostListView.as_view(), name='list'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('<slug>/', PostDetailView.as_view(), name='detail'),
    path('<slug>/update/', PostUpdateView.as_view(), name='update'),
    path('<slug>/delete/', PostDeleteView.as_view(), name='delete'),
    path('like/<slug>/', like, name='like'),
]
```

### Models

```python
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
    def comments(self):
        return self.comment_set.all()

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
```

### Views

```python
class PostDetailView(DetailView):
    model=Post

    def post(self, *args, **kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            comment = form.instance
            comment.user = self.request.user
            comment.post = post
            comment.save()
            return redirect('detail', slug=post.slug)
        return redirect('detail', slug=self.get_object().slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form': CommentForm
        })
        return context
    

    def get_object(self, **kwargs):
        obj = super().get_object(**kwargs)
        #if self.request.user.is_authenticated:
        PostView.objects.get_or_create(user=self.request.user, post=obj)
        return obj

class PostCreateView(CreateView):
    form_class=PostForm
    model=Post 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'create'
        }) 
        return context


def like(request,slug):
    post=get_object_or_404(Post, slug=slug)
    like_query_set=Like.objects.filter(user=request.user, post=post)
    if like_query_set.exists():
        like_query_set[0].delete()
        return redirect('detail', slug=slug)

    Like.objects.create(user=request.user, post=post)
    return redirect('detail', slug=slug)
        
```

### Forms

```python
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('__all__')

class CommentForm(forms.ModelForm):
    content=forms.CharField(required=True, widget=Textarea(attrs={
        'rows': 4
    }))
    class Meta:
        model=Comment
        fields=('content',)
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/Blog-With-Django-3.2.9-Full-Python-3.8. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).

```

```