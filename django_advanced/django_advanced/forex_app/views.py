from django.shortcuts import render
from django_advanced.forex_app.models import ForexData
import yfinance as yf

def forex_list(request):
    data = ForexData.objects.all()
    def get_forex_data():
        ticker = "EURUSD=X"
        forex_data = yf.Ticker(ticker)
        hist = forex_data.history(period="1d")
        return hist

    data_from_yfinance = get_forex_data()
    print(data_from_yfinance)
    return render(request, 'forex/forex_list.html', {'data': data, "title": "Forex Data 23123123 dsadsadasdasda"})