import time
from datetime import timedelta
from datetime import datetime
import requests
from flight_data import FlightData, find_cheapest
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint	import pprint
################################# Setting up##################################
data_manager = DataManager() # has get_sheet_data() in innit so returns it to self.sheet_data
flight_search = FlightSearch() # gets the token for amadues
sheet_data = data_manager.get_sheet_data() # one more step but better for understanding the code
notification_manager = NotificationManager()

# Getting customer emails
customer_data = data_manager.get_users_emails()
customer_email_list = [row['email'] for row in customer_data]

###################################### Iata Updating Iata Code#####################################

# for i in sheet_data:
# 	city_name = i["city"]
# 	if i["iataCode"] == "try again":
# 		iata_code= flight_search.get_iata_code(city_name)
# 		i["iataCode"] = iata_code
# 		# print(f"updated the iata to {iata_code}")
# 		print(city_name, iata_code)
# 	time.sleep(2)

# print("sheet data:\n", sheet_data)

# data_manager.sheet_data = sheet_data
# data_manager.update_iata_code()

################################### Flights data ##################################
tommorow = datetime.now() + timedelta(days=1)
reach_date = datetime.now() + timedelta(days=2*30)
origin_city = "UDR"

# Direct Flights
# for destination in sheet_data:
# 	# print("getting flights for", destination["city"], ":")
# 	flights_data = flight_search.check_flights(origin_city,from_time=tommorow , to_time=reach_date, destination= destination["iataCode"])
# 	# print(flights_data)
# 	time.sleep(1)
# 	cheapest_flight = find_cheapest(flights_data)
#
# 	# print(f"{destination['city']}: {cheapest_flight.price}")
#
# 	if cheapest_flight.price <= destination["lowestPrice"]:
# 		# print(f"lowest price found for {destination['city']}")
# 		# notification_manager.send_whatsapp(
# 		# 	body=f"Low price alert! Only £{cheapest_flight.price} to fly "
# 		# 				 f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
# 		# 				 f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}.")
# 		print(f"Low price alert! Only £{cheapest_flight.price} to fly "
# 						 f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
# 						 f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}.")
# 		time.sleep(2)
# 	elif cheapest_flight.price == float("inf"):
# 		print(f"NO direct flights looking for indirect flights for {destination['city']}")
# 		stopover_flights = flight_search.check_flights(
# 			origin_city,
# 			destination["iataCode"],
# 			from_time=tommorow,
# 			to_time=reach_date,
# 			is_direct=False
# 		)
# 		cheapest_flight = find_cheapest(stopover_flights)
# 		print(f"Cheapest indirect flight price is: {cheapest_flight.price} ")
# 		if cheapest_flight == float("inf"):
# 			print(f"Cant getch data or price for {destination['iataCode']}")
# 			continue
# 		print(f"Indirect flight found for {cheapest_flight.price} for {destination['city']}")
# 	else:
# 		print(f"Lowest price not found for {destination['city']} "
# 			  f"Price is at {cheapest_flight.price}")



