from django.contrib.auth.models import User
from django.db import models

# Create your models here.

def upload_to_profile(instance, filename):
    return f'profiles/{instance.user.username}/{filename}'

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    profile_picture = models.ImageField(upload_to=upload_to_profile,blank=True,null=True, default='profiles/default_pic_tb.jpg')
    bio = models.TextField(blank=True,)
    role = models.CharField(max_length=10,choices=[
        ('user', 'User'),
        ('staff', 'Staff'),
        ('admin', 'Administrator')
    ], default='user',
    )