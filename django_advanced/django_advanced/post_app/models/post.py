from django.db import models
from django.core.validators import MinLengthValidator
from django_advanced.user_app.models import Profile


class Post(models.Model):
    class Meta:
        ordering = ['-updated_at']
    
    title = models.CharField(
        unique=True,
        max_length=200,
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
        Profile,
        on_delete=models.CASCADE,
        related_name='posts'
    )
