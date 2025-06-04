from django.contrib import admin

from social.models import Like, Post, Comment


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['car', 'created_at']
    search_fields = ['car__model', 'car__owner__username']
    ordering = ['-created_at']
    list_filter = ['created_at']
    
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'created_at']
    search_fields = ['user__username', 'post__car__model']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'created_at']
    search_fields = ['user__username', 'description']
    list_filter = ['created_at']