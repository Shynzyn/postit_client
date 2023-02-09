from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.posts),
    path('posts', views.posts, name='posts'),
    path('post/<int:post_id>', views.post, name="post"),
    path('new_post', views.new_post, name="new_post"),
]
