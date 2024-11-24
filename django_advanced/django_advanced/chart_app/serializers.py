from rest_framework import serializers
from django_advanced.chart_app.models import ChartData

class ChartDataSerializer(serializers.ModelSerialier):
    class Meta:
        model = ChartData
        fields = '__all__'
