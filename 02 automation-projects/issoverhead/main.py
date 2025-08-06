import time

import requests
from datetime import datetime
import smtplib

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
my_email = "vipaschitattri@gmail.com"
password = "kotp ghtl lckq jpcn"


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def iss_above(iss_lat, iss_long, your_lat, your_long):
    if your_long-5 <= iss_long <= your_long+5 and your_lat-5 <= iss_lat <= your_lat+5:
        return


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

def send_mail():
    #If the ISS is close to my current position
    if iss_above(iss_latitude, iss_longitude, MY_LAT, MY_LONG) :
        if time_now.hour > sunset or time_now.hour < sunrise:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs="navyaattri6@gmail.com",
                                    msg=f"Subject: ISS location \n\n Look up ")
    else:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="navyaattri6@gmail.com",
                                msg=f"Subject: ISS location \n\n Look up afterwards ")

# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(5)
    send_mail()

