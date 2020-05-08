import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    appid = '6d4050ec69444e19183c61382e5f4bb7'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    cities = City.objects.all()
    oll_cities = []

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()
    form = CityForm

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }

        oll_cities.append(city_info)

    context = {'ol_info': oll_cities, 'form': form}
    return render(request, 'weatherapp/index.html', context)
