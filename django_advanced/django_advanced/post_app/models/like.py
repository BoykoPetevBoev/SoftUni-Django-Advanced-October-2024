from django.contrib.auth import get_user_model
from django.db import models
from django_advanced.post_app.models import Post


UserModel = get_user_model()


class Like(models.Model):
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )