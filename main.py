import json

from api import *
from global_url import *

if __name__ == '__main__':
    api = API()
    ##print("What date do you need to know?")
   ## date = input("Format: YYYY-MM-DD\n")
   ## print("When does Nils start his first lesson: ")
  ##  time = input("Format: HH:MM\n")
    response = api.calculate_trip(57.72002774943832, 12.932627629303825, "Borås Resecentrum", 57.68997981917106, 11.972944614985485, "Chalmers", "2022-04-09", "12:30")
    print(response["TripList"]["Trip"][0]["Leg"])
    print(response["TripList"]["Trip"][1]["Leg"][0]["Destination"]["time"])


#["TripList"]["Trip"]["Leg"][0]["Destination"]["time"]
