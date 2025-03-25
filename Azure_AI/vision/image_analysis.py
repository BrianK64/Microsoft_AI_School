from dotenv import load_dotenv
import os
import requests

# Microsoft Azure AI Services - Computer Vision Service - Image Analysis
class Image_Analysis():
    
    def __init__(self):

        # load environment variables
        load_dotenv()

        # Authentication credentials
        self.API_VISION_ENDPOINT = os.getenv("API_VISION_ENDPOINT")
        self.API_VISION_KEY = os.getenv("API_VISION_KEY")
        self.API_VISION_VERSION = os.getenv("API_VISION_VERSION")
        