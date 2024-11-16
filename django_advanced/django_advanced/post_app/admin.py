from django.contrib import admin
from django_advanced.post_app.models import Post, Comment, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class PostCommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class PostLikeAdmin(admin.ModelAdmin):
    pass
