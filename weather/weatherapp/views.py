import json
import urllib.request
import json
from django.shortcuts import render
from datetime import datetime  # Import the datetime module

def home(request):
    if request.method == 'POST':
        city = request.POST.get('city', 'True')

        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=164fec96a27b97680ee442e489ce3f06').read()
        list_of_data = json.loads(source)

        # Get the temperature in Celsius
        temperature_celsius = str(list_of_data['main']['temp']) + '°C'

        # Get the current date and time
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        context = {
            'city': city,
            'country_code': str(list_of_data['sys']['country']),
            'coordinate': str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
            'temp': temperature_celsius,  # Temperature in Celsius
            'pressure': str(list_of_data['main']['pressure']),
            'humidity': str(list_of_data['main']['humidity']),
            'current_datetime': current_datetime,  # Current date and time
        }
    else:
        context = {}

    return render(request, 'weatherapp/index.html', context)
