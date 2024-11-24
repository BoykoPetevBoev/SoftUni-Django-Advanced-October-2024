from django.urls import path
from .views import GoldPriceDataAPIView

urlpatterns = [
    path('', GoldPriceDataAPIView.as_view(), name='commodities'),
]

