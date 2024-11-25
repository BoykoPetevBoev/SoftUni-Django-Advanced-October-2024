from django.db import models
from django_advanced.user_app.models import Profile


class Portfolio(models.Model):
    profile = models.ForeignKey(
        Profile, 
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=100,
        unique=True,
        default=''
    )

    description = models.CharField(
        max_length=100,
        default=''
    )

    indices = models.DecimalField(
        max_digits=10,
        decimal_places=2, 
        default=0
    )
    stocks = models.DecimalField(
        max_digits=10,
        decimal_places=2, 
        default=0
    )
    commodities = models.DecimalField(
        max_digits=10,
        decimal_places=2, 
        default=0
    )
    cryptocurrency = models.DecimalField(
        max_digits=10,
        decimal_places=2, 
        default=0
    )
    forex = models.DecimalField(
        max_digits=10,
        decimal_places=2, 
        default=0
    )
    etfs = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
