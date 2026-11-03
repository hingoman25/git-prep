import os

import requests

WEATHERAPI_KEY = 'fb42d033b23840c086b190011260211'

location = input("Enter a city: ")
response = requests.get(
    "https://api.weatherapi.com/v1/current.json",
    params={"key": WEATHERAPI_KEY, "q": location},
    timeout=10,
)
response.raise_for_status()
temperature = response.json()["current"]["temp_c"]
print(f"Current temperature in {location}: {temperature} °C")