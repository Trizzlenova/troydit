from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
# from .forms import Form, SongForm
from .models import User, Post, Comment

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'troydit/post_list.html', {'posts': posts})
