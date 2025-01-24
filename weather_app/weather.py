# filepath: /path/to/your/file.py
import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('8c4b3cd33cf94c15b55221230251901')
city = 'London'
url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Error fetching weather data: {response.status_code}')
