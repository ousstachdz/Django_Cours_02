from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    content = models.CharField(max_length=200, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return self.content

class Message(models.Model):

    content = models.CharField(max_length=200, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return self.content

class Comment(models.Model):

    content = models.CharField(max_length=200, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return self.content


# Create your models here.
