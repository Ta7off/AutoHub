from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.views.generic import DetailView

from cars.models import Car
from social.forms import PostForm
from social.models import Post


def home(request):

    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'home/home.html', {"posts": posts})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'profile_user'



    def get_object(self, queryset=None):
        try:
            return self.get_queryset().get(username=self.kwargs['username'])
        except User.DoesNotExist:
            raise Http404("User not found")

def user_logout(request):
    logout(request)
    return redirect('home')

def post_creation(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})