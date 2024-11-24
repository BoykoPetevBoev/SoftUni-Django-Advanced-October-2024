from django.urls import path
from django_advanced.forex_app.views import forex_list

urlpatterns = [
    path('', forex_list, name='forex_list'),
]