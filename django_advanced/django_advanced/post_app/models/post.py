from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class Post(models.Model):
    class Meta:
        ordering = ['-updated_at']
    
    title = models.CharField(
        unique=True,
        max_length=50,
        validators=[
            MinLengthValidator(5),
        ]
    )
    
    image_url = models.URLField(
         help_text="Share your funniest furry photo URL!"
    )
    
    content = models.TextField()
    
    updated_at = models.DateTimeField(
        auto_now_add=True
    )
    
    author = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='posts'
    )
