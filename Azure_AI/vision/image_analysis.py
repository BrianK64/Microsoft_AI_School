from dotenv import load_dotenv
import os
import requests

# Microsoft Azure AI Services - Computer Vision Service - Image Analysis
class ImageAnalysisClient():
    

    def __init__(self):

        # load environment variables
        load_dotenv()

        # Authentication credentials
        self.API_VISION_ENDPOINT = os.getenv("API_VISION_ENDPOINT")
        self.API_VISION_KEY = os.getenv("API_VISION_KEY")

        # Query Parameters
        self.API_VISION_VERSION = os.getenv("API_VISION_VERSION")


    # Get the request URL from populated endpoint with query parameters
    def get_endpoint(self, *features):
        API_POPULATED_VISION_ENDPOINT = "{}imageanalysis:analyze?api-version={}&features={}".format(self.API_VISION_ENDPOINT, self.API_VISION_VERSION, ','.join(features))
        return API_POPULATED_VISION_ENDPOINT
    



    def image_analysis(self, image, *features):
        
        return


if __name__ == "__main__":
    client = ImageAnalysisClient()