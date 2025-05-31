from django.shortcuts import render, redirect, get_object_or_404

from .models import Post, Blog
from .forms import BlogForm, PostForm


# Create your views here.


def home(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "blogs/home.html", {"posts": posts})


def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = BlogForm()

    return render(request, "blogs/create_blog.html", {"form": form})


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostForm()
    return render(request, "blogs/create_post.html", {"form": form})


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostForm(instance=post)
    return render(request, "blogs/edit_post.html", {"form": form})
