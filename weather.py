import requests
import os


API_KEY = os.getenv('API_KEY') or ''
API_URL = (
    'http://api.openweathermap.org/data/2.5/weather?q={city_name}&mode=json&units=metric&appid={api_key}')


def query_api(city):
    try:
        print(API_URL.format(city_name=city, api_key=API_KEY))
        response = requests.get(API_URL.format(
            city_name=city, api_key=API_KEY)).json()

        print(response)

        # Check if the request was successful
        if response['cod'] == 200:
            return response
        else:
            print(f"Failed to retrieve data. HTTP Status code: {
                  response['cod']}")
            return None
    except Exception as exc:
        print(exc)
        response = None
        return response
