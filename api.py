import base64
import json
import requests
from global_url import *


def fetch_token(key, secret):
    # Every client using the api needs to pass a valid authentication key in every request.
    # How to generate token: https://developer.vasttrafik.se/portal/#/guides/oauth2

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic " + base64.b64encode((AUTH_KEY + ":" + AUTH_SECRET).encode()).decode()
    }

    data = {
        'grant_type': 'client_credentials'
    }

    serverData = requests.post(TOKEN_URL, data=data, headers=headers)

    # decode data to readable dictionary
    serverData = json.loads(serverData.content.decode('UTF-8'))
    return serverData["access_token"]


class API:

    def __init__(self):
        self.__authentication = fetch_token(AUTH_KEY, AUTH_SECRET)
        self.__format = "&format=json"

    def requestHTTP(self, location, querys=None):
        # Requests can only be made with GET

        headers = {
            "Authorization": "Bearer " + self.__authentication
        }

        url = BASE_URL + location

        if "?" not in url:
            url += "?"

        if querys is not None:
            for queryKey in querys:
                url += "&" + queryKey + "=" + str(querys[queryKey])

        url += "&" + self.__format

        response = requests.get(url, headers=headers)
        response = json.loads(response.content.decode('UTF-8'))

        return response

    def calculate_trip_data(self, originCoordLat, originCoordLong, originStreetName, destCoordLat, destCoordLong,
                       destStreetName, date, arrivalTime):
        location = "trip"

        querys = {
            "originCoordLat": originCoordLat,
            "originCoordLong": originCoordLong,
            "originCoordName": originStreetName,
            "destCoordLat": destCoordLat,
            "destCoordLong": destCoordLong,
            "destCoordName": destStreetName,
            "date": date,
            "time": arrivalTime,
            "searchForArrival": "1",
            "numTrips": "2"
        }

        response = self.requestHTTP(location, querys)
        return response

    def __getDifferenceInMinutes(self, lectureStart: str, busArrival: str):
        lectureTime = lectureStart.split(":")
        busArrivalTime = busArrival.split(":")
        self.__convertStringListToIntList(lectureTime)
        self.__convertStringListToIntList(busArrivalTime)

        lectureTimeMinutes = self.__convertTimeToMinutes(lectureTime)
        busArrivalTimeMinutes = self.__convertTimeToMinutes(busArrivalTime)

        return abs(lectureTimeMinutes - busArrivalTimeMinutes)

    def __convertTimeToMinutes(self, time):
        minutes = time[0] * 60 + time[1]
        return minutes

    def __convertStringListToIntList(self, listOfStringInt):
        for i in range(0, len(listOfStringInt)):
            listOfStringInt[i] = int(listOfStringInt[i])

        return listOfStringInt

    def getBusTimeIndex(self, lectureTime, lateBusArrival):
        if self.__getDifferenceInMinutes(lectureTime, lateBusArrival) < 10:
            return 0
        else:
            return 1
