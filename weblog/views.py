from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from weblog.models import Post, Comment


def main_page(req):
    all_posts = Post.objects.all()
    return HttpResponse(render(req, 'index.html', context={
        'posts': all_posts
    }))

def get_about(req):

    return HttpResponse(render(req, 'about.html', context={

    }))

def get_contact(req):

    return HttpResponse(render(req, 'contact.html', context={

    }))

def get_all_posts(req):
    all_posts = Post.objects.all()
    return HttpResponse(render(req, 'all_posts.html', context={
        'posts': all_posts
    }))


class CommentForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=20)
    text = forms.CharField(widget=forms.Textarea)


def get_single_post(req, post_id):
    if req.method == 'GET':
        post = Post.objects.get(id=post_id)
        return HttpResponse(render(req, 'single_post.html', context={
            'post': post,
            'comment_form': CommentForm()
        }))
    elif req.method == 'POST':
        # add comment
        form = CommentForm(data=req.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # TODO: fill the object creation logic(name, email, post, text)

            Comment.objects.create(
                name=form.cleaned_data['name'],

            )
            return HttpResponse("comment submitted")
        else:
            return HttpResponse("comment is invalid")


def author_profile(req, username):
    author = User.objects.get(username=username)
    posts = Post.objects.filter(author=author)
    return HttpResponse(render(req, 'author_profile.html', context={
        'posts': posts,
        'author': author,
    }))

