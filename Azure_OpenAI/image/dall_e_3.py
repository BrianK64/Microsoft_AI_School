#Imports
import os
import requests
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Access the environment variables
API_ENDPOINT = os.getenv("API_ENDPOINT")
API_KEY = os.getenv("API_KEY")

def request_dalle3(prompt):
    
    endpoint = API_ENDPOINT

    headers = {
        "api-key": API_KEY
    }

    body = {
        "prompt": prompt,
        "n": 1,
        "size": "1024x1024"
    }

    response = requests.post(endpoint, headers = headers, json = body)

    operation_location = response.headers["operation-location"]

    while 1:
        image_response = requests.get(operation_location, headers = headers)
        image_response_json = image_response.json()
        if image_response_json["status"] == "succeeded":
            image_url = image_response_json["result"]["data"][0]["url"]
            break
        time.sleep()

    return image_url