from django import forms
from .models import User, Post, Comment
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User



class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'image_url', 'description',)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'image_url', 'text')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'post', 'text')
