import base64
import io
from io import BytesIO
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import yfinance as yf


class GoldPriceDataAPIView(APIView):
    

    def fetch_gold_usd_data(self):
        # Fetch historical data for Gold (XAU/USD)
        gold = yf.Ticker("GC=F")  # GC=F is the symbol for Gold Futures
        data = gold.history(period="1d")  # Fetch data for today
        gold_data = yf.download('GC=F', period='6mo', progress=False)
        return gold_data
    


    def get(self, request):
        # Fetch Gold price data
        gold_data = self.fetch_gold_usd_data()

        # Prepare the data for the response (convert to HTML)
        gold_data_html = gold_data.sort_index(ascending=False).head(5).to_html()

        # Create the plot for the Gold price chart
        x = gold_data.index  # Timestamps
        y = gold_data['Close']  # Closing prices

        # Create the plot
        fig, ax = plt.subplots()
        ax.plot(x, y, label='Gold Price (USD)', color='gold')
        ax.set(xlabel='Time', ylabel='Price (USD)',
               title='Gold Price in USD')
        ax.grid()

        # Save the plot to a BytesIO buffer and encode it in base64
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        img_base64 = base64.b64encode(buffer.read()).decode('utf-8')

        # Return the HTML and image as a JSON response
        context = {
            'gold_data_html': gold_data_html,
            'gold_image_base64': img_base64,
        }
        return Response(context, status=status.HTTP_200_OK)