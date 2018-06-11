from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm, PostForm, CommentForm
from .models import User, Post, Comment

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'troydit/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'troydit/post_detail.html', {'post': post})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

@login_required
def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'troydit/post_form.html', {'form': form})

@login_required
def post_delete(request, pk):
    Post.objects.get(id=pk).delete()
    return redirect('post_list')

def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'troydit/comment_list.html', {'comments': comments})

def comment_detail(request, pk):
    comment = Comment.objects.get(id=pk)
    return render(request, 'troydit/comment_detail.html', {'comment': comment})

@login_required
def comment_create(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('comment_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'troydit/comment_form.html', {'form': form})

@login_required
def comment_edit(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect('comment_detail', pk=comment.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'troydit/comment_form.html', {'form': form})

@login_required
def comment_delete(request, pk):
    comment.objects.get(id=pk).delete()
    return redirect('comment_list')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'troydit/signup.html', {'form': form})
