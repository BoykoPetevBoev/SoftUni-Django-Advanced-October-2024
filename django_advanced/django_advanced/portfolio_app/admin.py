from django.contrib import admin
from django_advanced.portfolio_app.models import Portfolio

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    pass