from django.db import models

class ChartData(models.Model):
    ticker = models.CharField()
    symbol = models.CharField()
    pair = models.CharField()
