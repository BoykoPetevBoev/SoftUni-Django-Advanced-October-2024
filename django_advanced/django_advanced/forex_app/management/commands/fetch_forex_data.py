import yfinance as yf
from django.core.management.base import BaseCommand
from django_advanced.forex_app.models import ForexData

class Command(BaseCommand):
    help = 'Fetch forex data for USD pairs'

    def handle(self, *args, **kwargs):
        usd_pairs = ['EURUSD=X', 'GBPUSD=X', 'USDJPY=X', 'USDCHF=X', 'USDCAD=X', 'AUDUSD=X', 'NZDUSD=X']
        for pair in usd_pairs:
            data = yf.download(pair, period='1d', interval='1h')
            for index, row in data.iterrows():
                ForexData.objects.create(
                    pair=pair,
                    date=index.date(),
                    open=row['Open'],
                    high=row['High'],
                    low=row['Low'],
                    close=row['Close'],
                    volume=row['Volume']
                )
        self.stdout.write(self.style.SUCCESS('Successfully fetched forex data'))
