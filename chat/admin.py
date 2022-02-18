from django.contrib import admin

from .models import Message, Comment, Post

admin.site.register(Message)
admin.site.register(Post)
admin.site.register(Comment)
# Register your models here.
