from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.forms.models import model_to_dict
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def home(request):
    posts = Post.objects.all().order_by('-date_posted')  # newest first
    return render(request, 'blog/home.html', {'posts': posts})

# def getAllPosts(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/all_posts.html', {'posts': posts})

def getAllPosts(request):
    posts = Post.objects.all()
    posts_data = [model_to_dict(post) for post in posts]
    return render(request, 'blog/all_posts.html', {'posts_data': posts_data})

def create_post(request):
    if request.method == 'POST':
        print(type(request.POST))
        print(request.POST)
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-home')  # or 'all-posts'
    else:
        form = PostForm()

    return render(request, 'blog/create_post.html', {'form': form})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('all-posts')  # or 'blog-home'

    return render(request, 'blog/delete_post.html', {'post': post})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # creates the user
            return redirect('login')  # name of the login route from auth
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
