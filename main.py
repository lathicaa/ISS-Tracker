# Get the location of the ISS
import requests # making request object 
import json
import os
from dotenv import load_dotenv
from twilio.rest import Client
import math

load_dotenv()

def distance_haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in km
    
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    
    return distance

def get_Nasa_Data():
    global iss_latitude
    global iss_longitude

    # Contacting nasa servers 
    nasa_data = requests.get("http://api.open-notify.org/iss-now.json") #calling get method to read information from the nasa api

    # Turning a single string into keys and values, makes it readable 
    convert_nasa = json.loads(nasa_data.text) 

    # Parsing y to get specific data 
    iss_latitude = convert_nasa["iss_position"]["latitude"] 
    iss_longitude = convert_nasa["iss_position"]["longitude"]

    # Covert string to float
    iss_latitude = float(iss_latitude)
    iss_longitude = abs(float(iss_longitude))


def run():
    
    toronto_lat = 43.6532
    toronto_lon = 79.3832

    new_york_lat = 40.7128
    new_york_lon = 74.0060

    iss_distance_toronto = distance_haversine(toronto_lat, toronto_lon, iss_latitude, iss_longitude)
    new_york_distance_toronto = distance_haversine(toronto_lat, toronto_lon, new_york_lat, new_york_lon)


    winnipeg_lat = 49.8954
    winnipeg_lon = 97.1385

    minneapolis_lat = 44.977
    minneapolis_long = 93.2650

    iss_distance_winnipeg = distance_haversine(winnipeg_lat, winnipeg_lon, iss_latitude, iss_longitude)
    minneapolis_distance_winnipeg = distance_haversine(winnipeg_lat, winnipeg_lon, minneapolis_lat, minneapolis_long)


    vancouver_lat = 49.2827
    vancouver_lon = 123.1207

    calgary_lat = 51.0447
    calgary_lon = 114.0719

    iss_distance_vancouver = distance_haversine(vancouver_lat, vancouver_lon, iss_latitude, iss_longitude)
    calgary_distance_vancouver = distance_haversine(vancouver_lat, vancouver_lon, calgary_lat, calgary_lon)

    # Conditional to check if ISS above Toronto range
    if iss_distance_toronto <= new_york_distance_toronto:
        # Send SMS message to individual phone numbers
        account_sid = os.getenv("ACCOUNT_SID")
        auth_token = os.getenv("AUTH_TOKEN")
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='+18646190794',
            body=f'The ISS is currently above you! Latitude: {iss_latitude}°, Longitude: {iss_longitude}° ',
            to=os.getenv("LATHICA_NUMBER")
        )

        message = client.messages.create(
            from_='+18646190794',
            body=f'The ISS is currently above you! Latitude: {iss_latitude}°, Longitude: {iss_longitude}° ',
            to=os.getenv("ADITYA_NUMBER")
        )

        message = client.messages.create(
            from_='+18646190794',
            body=f'The ISS is currently above you! Latitude: {iss_latitude}°, Longitude: {iss_longitude}° ',
            to=os.getenv("KRISH_NUMBER")
        )

        #message = client.messages.create(
            #from_='+18646190794',
            #body=f'The ISS is currently above you! Latitude: {iss_latitude}°, Longitude: {iss_longitude}° ',
            #to=os.getenv("CLIENT_NUMBER")
        #)

    elif iss_distance_winnipeg <= minneapolis_distance_winnipeg:

        # Send SMS message to individual phone numbers
        account_sid = os.getenv("ACCOUNT_SID")
        auth_token = os.getenv("AUTH_TOKEN")
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='+18646190794',
            body=f'The ISS is approaching you in the next ten minutes! Latitude: {iss_latitude}°, Longitude: {iss_longitude}° ',
            to=os.getenv("LATHICA_NUMBER")
        )

        message = client.messages.create(
            from_='+18646190794',
            body=f'The ISS is appraoching you in the next ten minutes! Latitude: {iss_latitude}°, Longitude: {iss_longitude}° ',
            to=os.getenv("ADITYA_NUMBER")
        )

        message = client.messages.create(
            from_='+18646190794',
            body=f'The ISS is approaching you in the next ten minutes! Latitude: {iss_latitude}°, Longitude: {iss_longitude}° ',
            to=os.getenv("KRISH_NUMBER")
        )

        #message = client.messages.create(
            #from_='+18646190794',
            #body=f'The ISS is approaching you in the next ten minutes! Latitude: {iss_latitude}°, Longitude: {iss_longitude}° ',
            #to=os.getenv("CLIENT_NUMBER")
        #)


    elif iss_distance_vancouver <= calgary_distance_vancouver:

        # Send SMS message to individual phone numbers
        account_sid = os.getenv("ACCOUNT_SID")
        auth_token = os.getenv("AUTH_TOKEN")
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='+18646190794',
            body=f'The ISS is approaching you in the next half hour! Latitude: {iss_latitude}°, Longitude: {iss_longitude}° ',
            to=os.getenv("LATHICA_NUMBER")
        )

        message = client.messages.create(
            from_='+18646190794',
            body=f'The ISS is appraoching you in the next half hour! Latitude: {iss_latitude}°, Longitude: {iss_longitude}° ',
            to=os.getenv("ADITYA_NUMBER")
        )

        message = client.messages.create(
            from_='+18646190794',
            body=f'The ISS is approaching you in the next half hour! Latitude: {iss_latitude}°, Longitude: {iss_longitude}° ',
            to=os.getenv("KRISH_NUMBER")
        )

        #message = client.messages.create(
            #from_='+18646190794',
            #body=f'The ISS is approaching you in the next half hour! Latitude: {iss_latitude}°, Longitude: {iss_longitude}° ',
            #to=os.getenv("CLIENT_NUMBER")
        #)