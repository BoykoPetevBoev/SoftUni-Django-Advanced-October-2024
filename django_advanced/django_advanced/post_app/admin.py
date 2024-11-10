from django.contrib import admin
from django_advanced.post_app.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
