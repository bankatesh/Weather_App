from django.shortcuts import render, redirect
from .forms import *
from .models import *
import requests

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=1dfb9bce4d9bd00aaa581e488f5305f8'

    ncity = City.objects.all()
    form = CityForm()
    weather_data  =[]
    for city in ncity:
        r = requests.get(url.format(city)).json()
        # print(r.text)
        city_weather = {
            'city': city.name,
            'temprature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            'form': form,
            'ncity': ncity,

        }
        context = {'city_weather': city_weather}
        weather_data.append(city_weather)

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')




    return render(request, 'weather/weather.html', context)

