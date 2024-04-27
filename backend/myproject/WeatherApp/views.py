from django.shortcuts import render
import requests
from requests.exceptions import HTTPError

def weather(request):
    url = "http://api.weatherapi.com/v1/current.json?key=7f60cd198a0242e5a6d100948242504&q=London"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
    except HTTPError as http_err:
        # Handle HTTP errors like 404, 500, etc.
        print(f'HTTP error occurred: {http_err}')
        data = None
    except Exception as err:
        # Handle other errors like network issues, JSON decoding, etc.
        print(f'Other error occurred: {err}')
        data = None
    if data and isinstance(data, list) and len(data) > 0:
        context={
        'location': data[0]['location'] if data else {},
        'current': data[0]['current'] if data else {},
        }
    # } if data else{}  # If data is None, provide an empty context
    else:
        context = {}
    return render(request, 'WeatherApp/weather.html', context)
