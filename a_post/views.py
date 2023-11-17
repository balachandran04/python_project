from multiprocessing import context
from tkinter import NO
from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from a_post.models import *
from django import forms
from bs4 import BeautifulSoup
import requests
from django.contrib import messages
from .forms import *
from django.http import HttpResponse

# Create your views here.
def home(request,tag=None):
    if tag:
        posts = Post.objects.filter(tags__slug=tag)
        tag = get_object_or_404(Tag , slug=tag)
    else:   
        posts = Post.objects.all()
        
    categories = Tag.objects.all()
    context = {
        'post':posts,
        'categories': categories,
        'tag' : tag
    }    
    return render(request ,'a_posts/home.html', context)




@login_required
def post_create_view(request):
    form = PostCreateForm()

    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            website = requests.get(form.data['url'])
            sourcecode = BeautifulSoup(website.text, 'html.parser')


            find_image = sourcecode.select('meta[content^="https://live.staticflickr.com/"]')
            image = find_image[0]['content']
            post.image = image

            find_title = sourcecode.select('h1.photo-title')
            title = find_title[0].text.strip()
            post.title = title

            find_artist = sourcecode.select('a.owner-name')
            artist = find_artist[0].text.strip()
            post.artist = artist

            post.author = request.user

            post.save()
            form.save_m2m()
            return redirect('home')

    return render(request, 'a_posts/post_create.html', {'form': form})

@login_required
def post_delete_view(request,pk):
    post = get_object_or_404(Post, id=pk , author=request.user)
    if request.method == "POST":
        post.delete()
        messages.success(request ,'Post Was successfully Deleted')
        return redirect('home')
    return render(request, 'a_posts/post_delete.html', {'post' :post})

@login_required
def post_edit_view(request, pk):
    post = get_object_or_404(Post, id=pk, author=request.user)
    form = PostEditForm(instance=post)

    if request.method == "POST":
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid:
            form.save()
            messages.success(request, 'Post updated')
            return redirect('home')

    context = {
        'post': post,
        'form': form
    }
    return render(request, 'a_posts/post_edit.html', context)


def post_page_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    commentform = CommentCreateForm()
    replyform = ReplyCreateForm()

    if request.htmx:
        comments = post.comments.all()
        return render(request,'likes/loopage.html',{"comments":comments})
    context = {
        'post': post,
        'commentform': commentform,
        'replayform' : replyform
    }

    return render(request, 'a_posts/post_page.html',context)


@login_required
def comment_sent(request, pk):
    post = get_object_or_404(Post, id=pk)


    if request.method == 'POST':
        form = CommentCreateForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.author = request.user
            comment.parent_post = post
            comment.save()

    return redirect('post',post.id)

@login_required
def reply_sent(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    if request.method == 'POST':
        form = ReplyCreateForm(request.POST)
        if form.is_valid:
            reply = form.save(commit=False)
            reply.author = request.user
            reply.parent_comment = comment
            reply.save()

        return redirect('post',comment.parent_post.id)
    return render(request, 'a_posts/commend_delete.html', {'comment': comment})


@login_required
def comment_delete_view(request, pk):
    post = get_object_or_404(Comment, id=pk, author=request.user)

    if request.method == "POST":
        post.delete()
        messages.success(request, 'Comment deleted')
        return redirect('post', post.parent_post.id)

    return render(request, 'a_posts/commend_delete.html', {'comment': post})


def like_toggle(model):
    def inner_func(func):
        def wrapper(request, *args, **kwargs):
            post = get_object_or_404(model, id=kwargs.get('pk'))
            user_exist = post.likes.filter(username=request.user.username).exists()

            if post.author != request.user:
                if user_exist:
                    post.likes.remove(request.user)
                else:
                    post.likes.add(request.user)

            return func(request, post)
        return wrapper
    return inner_func
@login_required
@like_toggle(Post)
def like_post(request,post):
    return render(request, 'likes/likes.html', {'post' : post})
@login_required
@like_toggle(Comment)
def like_comment(request,post):
    return render(request, 'likes/likes_comment.html', {'comments' : post})





from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import RouteForm


def ContactForm(request):
    form = RouteForm()

    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            contact = form.cleaned_data['contact']
            form.save()

            html = render_to_string('includes/contact/contact.html', {
                'name': name,
                'email': email,
                'contact': contact
            })

            send_mail('the contact form subject', contact, 'balachantran8.com',['balachantran8 @ gmail.com'], html_message=html)
            return redirect('/')

    else:
        form = RouteForm()

    return render(request, 'includes/contactform.html', {'form': form})


def image(request, *args, **kwargs):
    image = Image.objects.all()
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ImageForm()

    context = {
        'form' :form,
        'image':image
    }


    return render(request,'includes/reels.html',context)


