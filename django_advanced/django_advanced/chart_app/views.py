import yfinance as yf
import matplotlib.pyplot as plt
import io
import base64
from django.shortcuts import render
from django.http import HttpResponse

def gold_price_chart(request):
    # Retrieve historical gold price data (GC=F is the ticker for Gold futures)
    gold_data = yf.download('GC=F', start='2023-01-01', end='2024-01-01', progress=False)

    # Create a plot
    plt.figure(figsize=(10, 6))
    plt.plot(gold_data['Close'], label='Gold Price (USD)', color='gold')

    # Add labels and title
    plt.title('Gold Price Over Time (2023)', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Price in USD', fontsize=12)

    # Rotate date labels for better readability
    plt.xticks(rotation=45)

    # Display a legend
    plt.legend()

    # Save the plot to a BytesIO object
    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)
    
    # Return the plot as an HTTP response
    return HttpResponse(img_buf, content_type='image/png')