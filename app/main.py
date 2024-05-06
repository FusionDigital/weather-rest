from fastapi import FastAPI
import json
import requests
from geopy.geocoders import Nominatim

def query_weather(input="New York City"):
    # Initialize the Nominatim API
    geolocator = Nominatim(user_agent="weather-rest")

    # Get the location of the city
    location = geolocator.geocode( input )

    url = "https://api.open-meteo.com/v1/forecast?latitude=%s&longitude=%s&hourly=precipitation&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,windspeed_10m_max&current_weather=true&timezone=%s&temperature_unit=%s&windspeed_unit=%s"  % (location.latitude, location.longitude, 'auto', 'fahrenheit', 'mph')
    raw = requests.get(url)
    response = json.loads(raw.text)
    return(raw.text)

app = FastAPI()

@app.get("/")
def root ():
    return { query_weather () }
@app.get("/zip/{location}")
async def read_item(location: int):
    return { query_weather ( location ) }
@app.get("/city")
def create_item(location: str):
    return { query_weather ( location ) }
