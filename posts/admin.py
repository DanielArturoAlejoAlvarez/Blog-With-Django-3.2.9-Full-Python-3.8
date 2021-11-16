from django.contrib import admin

from .models import Post,Comment,PostView,Like,User

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)
admin.site.register(Like)
