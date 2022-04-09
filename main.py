import json

from api import *
from global_url import *

if __name__ == '__main__':
    api = API()
    print("What date do you need to know?")
    date = input("Format: YYYY-MM-DD\n")
    print("When does Nils start his first lesson: ")
    time = input("Format: HH:MM\n")

    response = api.calculate_trip_data(57.72002774943832, 12.932627629303825, "Borås Resecentrum", 57.68997981917106, 11.972944614985485, "Chalmers", date, time)
    timePicker = api.getBusTimeIndex(time, response["TripList"]["Trip"][1]["Leg"][3]["Destination"]["time"])
    print("Nils is going to pick the bus that has its departure time: " + response["TripList"]["Trip"][timePicker]["Leg"][0]["Destination"]["time"])
