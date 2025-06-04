from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from cars.models import Car
from social.models import Post


def home(request):

    cars = Car.objects.all()

    return render(request, 'home/home.html', {"cars": cars})

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