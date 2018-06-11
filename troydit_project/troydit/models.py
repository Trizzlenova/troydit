from django.db import models
from django.contrib.auth.models import User, AbstractUser
from datetime import datetime

# Create your models here.

class User(AbstractUser):
    username = models.CharField(unique=True, blank=True, max_length=100)
    password = models.CharField(blank=True, max_length=100)
    image_url = models.TextField(blank=True, null=True)
    description = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.username.username

class Post(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=40)
    date = models.DateTimeField(default=datetime.now())
    image_url = models.TextField(blank=True, null=True)
    text = models.TextField()
    vote = 0


    def __str__(self):
      return self.title


class Comment(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    date = models.DateTimeField(default=datetime.now())
    text = models.TextField()

    def __str__(self):
      return self.text

