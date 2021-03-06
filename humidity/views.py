from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import HumidityForm
from django.utils import timezone

import datetime

today = datetime.date.today()
now = timezone.localtime(timezone.now())
month = today.month

from .models import Humidity
from graphos.sources.model import ModelDataSource
from graphos.renderers import gchart

def index(request):


    queryset = Humidity.objects.all().order_by('-id')[:1]
    data_source = ModelDataSource(queryset, fields=['Humidity_Percent'])
    humidity_chart = gchart.GaugeChart(data_source,
            options = {
               "greenFrom": 90, "greenTo": 100,
                "yellowFrom": 75, "yellowTo": 90,
                "redFrom": 65, "redTo": 75,
                "max": 100, "majorTicks": [0,20,40,60,80,100], "minorTicks": 10,
            }
    )

    return render(request, 'humidity/index.html', {'humidity_chart': humidity_chart})

def input(request):
    if request.method == 'POST':
        form = HumidityForm(request.POST)
        if form.is_valid():
            humidity = request.POST.get('new_humidity', '')
            humidity_obj = Humidity( Humidity_Percent = humidity, reading_time = now )
            humidity_obj.save()

        return HttpResponseRedirect(reverse('humidity:thanks'))

    else:
        form = HumidityForm()
    return render(request, 'humidity/input.html', {'form': form, 'form': form})

def thanks(request):
    return render(request, 'humidity/thanks.html')

def daily(request):

    queryset = Humidity.objects.filter(reading_time__date=today)
    data_source = ModelDataSource(queryset, fields=['reading_time', 'Humidity_Percent'])
    humidity_daily_line_chart = gchart.LineChart(data_source, options={'title': "Daily Readings"})

    return render(request, 'humidity/daily.html', {'humidity_daily_line_chart': humidity_daily_line_chart})

def monthly(request):

    queryset = Humidity.objects.filter(reading_time__month=month)
    data_source = ModelDataSource(queryset, fields=['reading_time', 'Humidity_Percent'])
    humidity_monthly_line_chart = gchart.LineChart(data_source, options={'title': "Monthly Readings"})

    return render(request, 'humidity/monthly.html', {'humidity_monthly_line_chart': humidity_monthly_line_chart})
