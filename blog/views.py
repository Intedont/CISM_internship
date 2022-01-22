from django.shortcuts import render
from blog.forms import SignUpForm, NewPostForm, CommentForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from blog.models import Post, Comment
from django.contrib.auth.decorators import login_required
import datetime
from django.db.models import QuerySet
# Create your views here.

def index(request):
    posts = Post.objects.filter(isActive=1).order_by('-date')
    ids = []
    for post in posts:
        ids.append(post.id)
    print("IDS")
    print(ids)
    comments = Comment.objects.filter(post_id__in=ids).order_by('-date')[:6][::-1]
    print("COMMENTS")
    for comment in comments:
        print(comment)

    context ={
        'username': request.user,
        'posts': posts,
        'comments': comments,
        'form': CommentForm()
    }
    return render(request, 'index.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, password=password)
            user.save()

            return redirect('/login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form, 'username': request.user})


def profile(request, username):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = Post(text=form.cleaned_data.get('text'),
                        title=form.cleaned_data.get('title'),
                        author=request.user,
                        date=datetime.datetime.now())
            post.save()
        return redirect('/accounts/' + request.user.username)
    else:
        posts = Post.objects.filter(author=User.objects.get(username=username))
        posts = posts.exclude(isActive=0).order_by('-date')
        context = {
            'username': request.user,
            'posts': posts,
            'viewed_username': username,
            'form': NewPostForm()
        }
        print(context['username'])
        return render(request, 'profile.html', context)

@login_required(login_url='/login')
def like(request, id):
    post = Post.objects.get(id=id)
    post.likes += 1
    post.save()

    return redirect('/')

@login_required(login_url='/login')
def delete(request, id):
    post = Post.objects.get(id=id)
    if post.author == request.user:
        if post.isActive == 1:
            post.isActive = 0
            post.save()
        else:
            post.delete()
    return redirect('/accounts/' + request.user.username)


@login_required(login_url='/login')
def wastebin(request):
    posts = Post.objects.filter(author=request.user).filter(isActive=0)

    context = {
        'posts': posts,
        'username': request.user
    }

    return render(request, 'wastebin.html', context)

@login_required(login_url='/login')
def restore(request, id):
    post = Post.objects.get(id=id)
    if post.author == request.user:
        post.isActive = 1
        post.save()
    return redirect('/wastebin/')


@login_required(login_url='/login')
def addComment(request, id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data.get('text'),
                              post=Post.objects.get(id=id),
                              author=request.user,
                              date=datetime.datetime.now())
            comment.save()
        return redirect('/')