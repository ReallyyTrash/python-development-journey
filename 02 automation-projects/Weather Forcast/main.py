import requests
from twilio.rest import Client

account_sid = 'AC50045f59fab9aa7b861951889d2f940b'
auth_token = '[787be373797e2f134d76b0054263df07]'



api_key = "ec9748c809debe9bb8306882a6ee08a3"
lat = 24.585445
lon= 73.712479
api_call = "https://api.openweathermap.org/data/2.5/forecast"

paramerters= {
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
        body= "bring umbrella"
    )

    print(message.status)