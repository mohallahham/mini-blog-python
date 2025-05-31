from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden


from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


from .models import Post, Blog
from .forms import BlogForm, PostForm, UserRegisterForm


# Create your views here.


def home(request):
    posts = Post.objects.all().order_by("-created_at")  # 👈 Show ALL posts
    return render(request, "blogs/home.html", {"posts": posts})


@login_required
def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.owner = request.user
            blog.save()
            return redirect("home")
    else:
        form = BlogForm()
    return render(request, "blogs/create_blog.html", {"form": form})


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("home")
    else:
        form = PostForm()
    return render(request, "blogs/create_post.html", {"form": form})


@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:  # 👈 Check the Post author now
        return HttpResponseForbidden("You are not allowed to edit this post.")

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostForm(instance=post)
    return render(request, "blogs/edit_post.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserRegisterForm()
    return render(request, "blogs/register.html", {"form": form})
