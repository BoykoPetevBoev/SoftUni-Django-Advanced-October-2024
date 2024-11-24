from django.db import models
from django_advanced.post_app.models import Post
from django_advanced.user_app.models import Profile


class Like(models.Model):
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name='likes'
    )