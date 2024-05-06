import sys
import json

import requests
from geopy.geocoders import Nominatim


my_prompt = "New York City"
if len(sys.argv) == 2:
    my_prompt = sys.argv[1] 



def query_weather(input="New York City"):
    # Initialize the Nominatim API
    geolocator = Nominatim(user_agent="weather-rest")

    # Get the location of the city
    location = geolocator.geocode( input )

    url = "https://api.open-meteo.com/v1/forecast?latitude=%s&longitude=%s&hourly=precipitation&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,windspeed_10m_max&current_weather=true&timezone=%s&temperature_unit=%s&windspeed_unit=%s"  % (location.latitude, location.longitude, 'auto', 'fahrenheit', 'mph')
    raw = requests.get(url)
    response = json.loads(raw.text)
    print (response)

    print(f"Coordinates {response['latitude']}°N {response['longitude']}°E")
    print(f"Elevation {response['elevation']} m asl")
    print(f"Timezone {response['timezone']} {response['timezone_abbreviation']}")
    print(f"Timezone difference to GMT+0 {response['utc_offset_seconds']} s")

    return(raw.text)

if __name__ == '__main__':
    # executed as script
    query_weather(my_prompt or null) 
