import os, requests
from pprint import pprint
from typing import Any

FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
class FlightSearch:
	#This class is responsible for talking to the Flight Search API.
	def __init__(self):
		from dotenv import load_dotenv
		load_dotenv()
		self.api_key = os.getenv("AMADUES_APIKEY")
		self.api_id = os.getenv("AMADUES_ID")
		self.amadues_token = self.get_new_token()

	def get_iata_code(self, city: str) -> str:
		iata_endpoint="https://test.api.amadeus.com/v1/reference-data/locations"
		param = {
			"keyword": city,
			"subType": "CITY"
		}
		header={
			"Authorization": f"Bearer {self.amadues_token}"
		}
		response = requests.get(iata_endpoint, headers=header, params=param)
		response.raise_for_status()
		data = response.json()

		if data.get("data"):
			try:
				return data["data"][0]["iataCode"]
			except (IndexError, KeyError):
				print(f"No iata code found for {city}")
				return "try again"
		else:
			print(f"{city} : {data['data']}")

	def get_new_token(self):

		amadues_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
		amadues_headers = {
			"Content-Type": "application/x-www-form-urlencoded"
		}
		amadues_data_para = {
			"grant_type": "client_credentials",
			"client_id": self.api_id,
			"client_secret": self.api_key}

		response = requests.post(amadues_endpoint, data=amadues_data_para, headers=amadues_headers)
		return response.json()['access_token']

	def check_flights(self, origin_city, destination, from_time, to_time, is_direct: bool = True):
		header = {
			"Authorization": f"Bearer {self.amadues_token}"
		}
		query = {
			"originLocationCode": origin_city,
			"destinationLocationCode": destination,
			"departureDate": from_time.strftime("%Y-%m-%d"),
			"returnDate": to_time.strftime("%Y-%m-%d"),
			"adults": 1,
			"nonStop": "true" if is_direct else "false",
			"currencyCode": "INR",
			"max": "10",
		}
		response = requests.get(url=FLIGHT_ENDPOINT,headers=header,params=query,)
		return response.json()
