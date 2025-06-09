from django.shortcuts import render, get_object_or_404, redirect

from social.models import Post, Comment


# Create your views here.

def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('home')

def add_comment(request,post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        content = request.POST.get('description')
        Comment.objects.create(post=post, user=request.user, description=content)

    return redirect('home')