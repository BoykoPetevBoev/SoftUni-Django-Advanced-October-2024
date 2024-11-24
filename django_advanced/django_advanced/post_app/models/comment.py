from django.db import models
from django_advanced.post_app.models import Post
from django_advanced.user_app.models import Profile


class Comment(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['date_time_of_publication']),
        ]
        ordering = ['-date_time_of_publication']

    text = models.TextField(
        max_length=300,
    )

    date_time_of_publication = models.DateTimeField(
        auto_now_add=True,
    )

    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name='comments'
    )
