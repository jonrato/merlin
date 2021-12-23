from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import StockData

import requests
import json

APIKEY = '9H3L5CFY26CVAR3M'

DATABASE_ACCESS = True

def home(request):
    return render(request, 'stockVisualizer/home.html', {})

@csrf_exempt
def get_stock_data(request):
    if request.is_ajax():
        ticker = request.POST.get('ticker','null')
        ticker = ticker.upper()

        if DATABASE_ACCESS == True:
            if StockData.objects.filter(symbol=ticker).exists():
                entry = StockData.objects.filter(symbol=ticker)[0]
                return HttpResponse(entry.data, content_type='application/json')
        
        price_series=requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&apikey={APIKEY}&outputsize=full').json()
        sma_series = requests.get(f'https://www.alphavantage.co/query?function=SMA&symbol={ticker}&interval=1min&series_type=close&apikey={APIKEY}').json()
        #av_fun="TIME_SERIES_INTRADAY", interval="30min"
        output_dictionary = {}
        output_dictionary['prices'] = price_series
        output_dictionary['sma'] = sma_series

        temp = StockData(symbol=ticker, data=json.dumps(output_dictionary))
        temp.save()

        return HttpResponse(json.dumps(output_dictionary), content_type='application/json')
    else:
        message = "Not Ajax"
        return HttpResponse(message)
