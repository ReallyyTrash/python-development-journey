import requests
class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin, destination, out, return_date, stops):
        self.price = price
        self.origin_airport = origin
        self.destination_airport = destination
        self.out_date = out
        self.return_date = return_date
        self.stops = stops
def find_cheapest(data):
    # Data doesnt exist = Either STOP problem or API problem i guesss
    if data is None or "data" not in data or not data["data"]:
        print("[DEBUG] No flights found or bad response.")
        return FlightData(float("inf"), "N/A", "N/A", "N/A", "N/A", stops="N/A")

    # # Data from the first flight in the json
    # Dont know if else is needed but still using
    # WHy are we using first flight and setting it as cheapest_flight? Is there a possibilty that first flight can be missed in out for loop for checkng flights
    else:
        first_flight = data['data'][0]
        lowest_price = float(first_flight["price"]["grandTotal"])
        nr_stops = len(first_flight["itineraries"][0]["segments"]) - 1 ## ?? What is this how is this not 0 what is actualyy in the data
        origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
        destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
        out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
        return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

        cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, stops=nr_stops)
        # check for flights Min Price
        for flights in data['data']:
            try:
                price = float(flights["price"]["grandTotal"])
                if price <= lowest_price:
                    lowest_price = price
                    origin = flights["itineraries"][0]["segments"][0]["departure"]["iataCode"]
                    destination = flights["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
                    out_date = flights["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
                    return_date = flights["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
                    nr_stops = len(flights["itineraries"][0]["segments"]) - 1
                    # DOUBT in adding stops
                    cheapest_flight = FlightData(price, origin, destination, out_date, return_date, stops=nr_stops)
            except (KeyError, IndexError) as e: # WHat does these Error actually mean? can I use them according to my need
                print("error with data limit ")
                continue # what is the need for this

    return cheapest_flight

