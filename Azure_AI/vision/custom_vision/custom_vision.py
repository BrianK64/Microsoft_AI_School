# Imports
from dotenv import load_dotenv
import os

# Custom Vision
class CustomVisionClient():

    def __init__(self):
        
        # load environment variables

        # set up custom vision authentication credentials
        API_CUSTOM_VISION_TRAINING_ENDPOINT = os.getenv("API_CUSTOM_VISION_TRAINING_ENDPOINT")
        API_CUSTOM_VISION_TRAINING_KEY = os.getenv("API_CUSTOM_VISION_TRAINING_KEY")
        API_CUSTOM_VISION_PREDICTION_ENDPOINT = os.getenv("API_CUSTOM_VISION_PREDICTION_ENDPOINT")
        API_CUSTOM_VISION_PREDICTION_KEY = os.getenv("API_CUSTOM_VISION_PREDICTION_KEY")
        API_CUSTOM_VISION_PREDICTION_RESOURCE_ID = os.getenv("API_CUSTOM_VISION_PREDICTION_RESOURCE_ID")


if __name__ == "__main__":
    client = CustomVisionClient()