from django import forms
from .models import Blog, Post

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["name", "description"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["blog", "title", "content"]


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
