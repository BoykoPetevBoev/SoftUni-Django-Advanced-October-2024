from django.contrib import admin
from django_advanced.chart_app.models import ChartData

@admin.register(ChartData)
class ChartDataAdmin(admin.ModelAdmin):
    pass
