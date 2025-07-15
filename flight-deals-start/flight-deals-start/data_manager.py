import requests, os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")

sheety_url = "https://api.sheety.co/6345ce058d753cb5ab0cc05218250a9d/copyOfFlightDeals/prices"
auth_header = {f"Authorization": f"Bearer {SHEETY_TOKEN}"}
USERS_ENDPOINT = "https://api.sheety.co/6345ce058d753cb5ab0cc05218250a9d/copyOfFlightDeals/users"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.customer_data = None
        self.sheet_data = None

    def get_sheet_data(self):
        response = requests.get(url=sheety_url, headers=auth_header)
        self.sheet_data = response.json()["prices"]
        return self.sheet_data

    def update_iata_code(self):
        for i in self.sheet_data:
            new_data={
                "price": {
                    "iataCode": i["iataCode"]
                }
            }
            response = requests.put(url=f"{sheety_url}/{i['id']}", json=new_data, headers=auth_header)
            response.raise_for_status()
    def get_users_emails(self):
        response = requests.get(USERS_ENDPOINT)
        data = response.json()
        self.customer_data = data['users']
        return self.customer_data
