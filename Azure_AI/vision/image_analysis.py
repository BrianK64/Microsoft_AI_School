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
        self.API_VISION_VERSION = os.getenv("API_VISION_VERSION")


    # Get the request URL from populated endpoint with query parameters
    def get_endpoint(self, features, language = "en-US"):

        # Query Parameters
        query_params = {
            "api-version": self.API_VISION_VERSION,
            "features": ','.join(features),
            "language": language
        }

        API_POPULATED_VISION_ENDPOINT = "{}computervision/imageanalysis:analyze?api-version={}&features={}".format(self.API_VISION_ENDPOINT, self.API_VISION_VERSION, ','.join(features))
        return API_POPULATED_VISION_ENDPOINT
    

    # Configure HTTP request
    def send_request(self, method, url, json):

        headers = {
            "Ocp-Apim-Subscription-Key": self.API_VISION_KEY,
            "Content-Type":"application/json"
        }

        # HTTP call and error handling
        try:
            response = requests.request(method = method,url = url, headers = headers, json = json if isinstance(json, dict) else None, data = None if isinstance(json, dict) else json)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as error:
            print("Invalid Request: {}".format(error))
            raise

    def image_analysis(self, image, features):
        
        endpoint = self.get_endpoint(features)
        payload = {"url": image} if isinstance(image, str) else open(image, "rb").read()

        response = self.send_request("POST", endpoint, payload)

        return response


if __name__ == "__main__":
    client = ImageAnalysisClient()
    image_url = "https://learn.microsoft.com/azure/cognitive-services/computer-vision/images/windows-kitchen.jpg"
    features = ["caption", "tags", "denseCaptions", "objects"]
    response = client.image_analysis(image=image_url, features = features)
    print(response)