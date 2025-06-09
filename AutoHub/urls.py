"""
URL configuration for AutoHub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from social.views import like_post, add_comment
from . import views
from .views import register, ProfileView, user_logout, post_creation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
    path('create/', post_creation, name='create_post'),
    path('post/<int:post_id>/like/', like_post, name='like_post'),
    path('post/<int:post_id>/comment/', add_comment, name='add_comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
