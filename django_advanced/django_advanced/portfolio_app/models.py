from django.db import models
from django_advanced.user_app.models import Profile

ASSET_TYPE_CHOICES = [
    ('indices', 'Indices'),
    ('stocks', 'Stocks'),
    ('commodities', 'Commodities'),
    ('cryptocurrency', 'Cryptocurrency'),
    ('forex', 'Forex'),
    ('etfs', 'ETFs'),
]

class Portfolio(models.Model):
    profile = models.ForeignKey(
        Profile, 
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=100,
        default=''
    )

    description = models.CharField(
        max_length=100,
        default=''
    )
    
    assetType = models.CharField(
        max_length=100,
        choices=ASSET_TYPE_CHOICES,
        default='forex'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    
    def get_latest_balance(self):
        daily_price = self.daily_prices.first()
        return daily_price
    
    def get_dates(self):
        daily_prices = self.daily_prices.all()
        if daily_prices:
            return [price.date for price in self.daily_prices.all()]
        return []

    def get_balance(self):
        daily_prices = self.daily_prices.all()
        if daily_prices:
            return [price.balance for price in daily_prices ]
        return []


class DailyPrice(models.Model):
    date = models.DateField()
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    comment = models.CharField(max_length=100, default='', blank=True)
    portfolio = models.ForeignKey(
       Portfolio, 
        related_name='daily_prices',  # This is the reverse relation from Portfolio to DailyPrice
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f"{self.date} - {self.balance}"
    
    class Meta:
        ordering = ['-date']


    # indices = models.DecimalField(
    #     max_digits=10,
    #     decimal_places=2, 
    #     default=0
    # )
    # stocks = models.DecimalField(
    #     max_digits=10,
    #     decimal_places=2, 
    #     default=0
    # )
    # commodities = models.DecimalField(
    #     max_digits=10,
    #     decimal_places=2, 
    #     default=0
    # )
    # cryptocurrency = models.DecimalField(
    #     max_digits=10,
    #     decimal_places=2, 
    #     default=0
    # )
    # forex = models.DecimalField(
    #     max_digits=10,
    #     decimal_places=2, 
    #     default=0
    # )
    # etfs = models.DecimalField(
    #     max_digits=10,
    #     decimal_places=2,
    #     default=0
    # )