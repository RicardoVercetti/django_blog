from django.urls import path
from . import views

urlpatterns = [
    path('all-posts', views.getAllPosts, name='all-posts'),
    path('', views.home, name='blog-home'),
    path('create/', views.create_post, name='create-post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete-post'),
    path('register/', views.register, name='register'),
]
