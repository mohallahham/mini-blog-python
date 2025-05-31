from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create_blog/", views.create_blog, name="create_blog"),
    path("create_post/", views.create_post, name="create_post"),
    path("edit_post/<int:pk>/", views.edit_post, name="edit_post"),
]
