
# Get the location of the ISS
import requests # making request object 
import json
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

nasa_data = requests.get("http://api.open-notify.org/iss-now.json") #calling get method to read information from the nasa api
#contacting nasa servers 

convert_nasa = json.loads(nasa_data.text) 
#turning a single string into keys and values, makes it readable 

iss_latitude = convert_nasa["iss_position"]["latitude"] #parsing y to get specific data 
iss_longitude = convert_nasa["iss_position"]["longitude"]

# covert string to float
iss_latitude = float(iss_latitude)
iss_longitude = float(iss_longitude)

#43.505085, -80.702434
# conditional to check if ISS above Toronto range
if abs(iss_latitude - 43.6532) <= abs(43.4730 - 43.6532) and abs(iss_longitude - 79.3832 ) <= abs(80.5395 - 79.3832):
    token = os.getenv("AUTH_TOKEN")

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

