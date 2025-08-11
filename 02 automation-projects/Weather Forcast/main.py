import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
api_key = os.getenv("API_KEY")
lat = 24.585445
lon = 73.712479
api_call = "https://api.openweathermap.org/data/2.5/forecast"

paramerters = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "cnt": 12,
}

response = requests.get(api_call, params=paramerters)
response.raise_for_status()
weather_data = response.json()
raining = False
for i in range(12):
    if weather_data["list"][i]['weather'][0]['id'] < 700:
        raining = True

if raining:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+12294583349',
        to='+916350015420',
        body="bring umbrella"
    )

    print(message.status)