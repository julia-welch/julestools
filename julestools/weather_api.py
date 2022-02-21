# pylint: disable=missing-module-docstring

import sys
import requests

BASE_URI = "https://www.metaweather.com"


def search_city(query):
    '''Look for a given city and disambiguate between several candidates.
    Return one city (or None)'''
    url = "https://www.metaweather.com/api/location/search/?query={}".format(query)
    response = requests.get(url).json()
    if response == []:
        return None
    city_info = response[0]
    return city_info

def weather_forecast(woeid):
    '''Return a 5-element list of weather forecast for a given woeid'''
    url = "https://www.metaweather.com/api/location/{}/".format(woeid)
    response = requests.get(url).json()
    return response["consolidated_weather"]


def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city = search_city(query)

    woeid = city["woeid"]
    c_w_list = weather_forecast(woeid)
    forecasts = []

    for index, fc in enumerate(c_w_list):
        if index < 5:
            forecasts.append(f'{fc["applicable_date"]}: {fc["weather_state_name"]} {round(fc["the_temp"], 0)}°C')

    print(f'Here\'s the weather in {city["title"]}')
    for f in forecasts:
        print(f)


if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
