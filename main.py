import json

from api import *
from global_url import *

if __name__ == '__main__':
    api = API()
    response = api.calculate_trip(57.72002774943832, 12.932627629303825, "Borås Resecentrum", 57.68997981917106, 11.972944614985485, "Aschebergsgatan", "2022-04-09", "10:00")
    print(response["TripList"]["Trip"]["Leg"][0]["Origin"]["time"])
    pass


