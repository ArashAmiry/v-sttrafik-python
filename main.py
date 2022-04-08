import json

from api import *
from global_url import *

if __name__ == '__main__':
    api = API()
    response = api.calculate_trip(57.73167124475054, 12.99941225629025, "Grandgatan", 57.68997981917106, 11.972944614985485, "Aschebergsgatan", "2022-04-09", "11:30")
    print(response)
    pass


