from django.contrib.auth.models import User
from django.db import models

from cars.models import Car


# Create your models here.


def upload_to_post(instance, filename):
    return f'posts/{instance.car.owner.username}/{instance.car.id}/{filename}'


class Post(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to=upload_to_post, null=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def __str__(self):
        return f"Post of {self.car}"

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f"{self.user.username} liked {self.post}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post}"