import json

from api import *
from global_url import *

if __name__ == '__main__':
    api = API()
    query = {
        "originCoordLong": 11.981211,
        "originCoordLat": 57.709792
    }
    response = api.requestHTTP("location.nearbystops", query)
    print(response)
    pass


