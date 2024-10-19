
# Get the location of the ISS
import requests # making request object 
import json
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()



def get_Nasa_Data():
    global iss_latitude
    global iss_longitude

    nasa_data = requests.get("http://api.open-notify.org/iss-now.json") #calling get method to read information from the nasa api
    #contacting nasa servers 

    convert_nasa = json.loads(nasa_data.text) 
    #turning a single string into keys and values, makes it readable 

    iss_latitude = convert_nasa["iss_position"]["latitude"] #parsing y to get specific data 
    iss_longitude = convert_nasa["iss_position"]["longitude"]

    # covert string to float
    iss_latitude = float(iss_latitude)
    iss_longitude = float(iss_longitude)


def run():
    #40.7128° N, 74.0060° W NEW YORK
    #43.6532° N, 79.3832° W TORONTO
    # conditional to check if ISS above Toronto range
    if abs(iss_latitude - 43.6532) <= abs(43.4730 - 40.7128) and abs(iss_longitude - 79.3832) <= abs(79.3832 - 74.0060):
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

        #message = client.messages.create(
            #from_='+6475511906',
            #body=f'The ISS is currently above you! Latitude: {iss_latitude}°, Longitude: {iss_longitude}° ',
            #to=os.getenv("KRISH_NUMBER")
        #)

        #message = client.messages.create(
            #from_='+',
            #body=f'The ISS is currently above you! Latitude: {iss_latitude}°, Longitude: {iss_longitude}° ',
            #to=os.getenv("NAME_NUMBER")
        #)

    #49.8954° N, 97.1385° W WINNIPEG
    #44.9778° N, 93.2650° W MINNEAPOLIS
    elif abs(iss_latitude - 49.8954) <= abs(49.8954 - 44.9778) and abs(iss_longitude - 97.1385) <= abs(97.1385 - 93.2650):

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

        #message = client.messages.create(
            #from_='+6475511906',
            #body=f'The ISS is approaching you in the next ten minutes! Latitude: {iss_latitude}°, Longitude: {iss_longitude}° ',
            #to=os.getenv("KRISH_NUMBER")
        #)

        #message = client.messages.create(
            #from_='+',
            #body=f'The ISS is approaching you in the next ten minutes! Latitude: {iss_latitude}°, Longitude: {iss_longitude}° ',
            #to=os.getenv("NAME_NUMBER")
        #)

    #49.2827° N, 123.1207° W VANCOUVER
    #51.0447° N, 114.0719° W CALGARY
    elif abs(iss_latitude - 49.2827) <= abs(49.2827 - 51.0447) and abs(iss_longitude - 123.1207) <= abs(123.1207 - 114.0719):

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

        #message = client.messages.create(
            #from_='+6475511906',
            #body=f'The ISS is approaching you in the next half hour! Latitude: {iss_latitude}°, Longitude: {iss_longitude}° ',
            #to=os.getenv("KRISH_NUMBER")
        #)

        #message = client.messages.create(
            #from_='+',
            #body=f'The ISS is approaching you in the next half hour! Latitude: {iss_latitude}°, Longitude: {iss_longitude}° ',
            #to=os.getenv("NAME_NUMBER")
        #)


