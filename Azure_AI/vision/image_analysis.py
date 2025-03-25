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


    # Get the HTTP request URL and query parameters
    def get_endpoint(self, features, language, smartcrops_aspect_ratios):

        # Query Parameters
        query_params = {
            "api-version": self.API_VISION_VERSION,
            "features": ','.join(features),
            "language": language
        }

        if "smartCrops" in features:
            query_params.update(
                {
                    "smartcrops-aspect-ratios": smartcrops_aspect_ratios
                }
            )

        endpoint = "{}computervision/imageanalysis:analyze".format(self.API_VISION_ENDPOINT)
        return endpoint, query_params
    

    # Configure HTTP request
    def send_request(self, method, url, params, json):

        isImageURL = True if isinstance(json, dict) else False

        headers = {
            "Ocp-Apim-Subscription-Key": self.API_VISION_KEY,
            "Content-Type": "application/json" if isImageURL else "application/octet-stream"
        }

        # HTTP call and error handling
        try:
            response = requests.request(method = method, url = url, params = params, headers = headers, json = json if isImageURL else None, data = None if isImageURL else json)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as error:
            print("Invalid Request: {}".format(error))
            raise

    def image_analysis(self, image, features, language = "en", smartcrops_aspect_ratios = ""):
        
        endpoint, query_params = self.get_endpoint(features, language, smartcrops_aspect_ratios)
        payload = {"url": image} if isinstance(image, str) else open(image, "rb").read()

        response = self.send_request(method = "POST", url = endpoint, params = query_params, json = payload)

        return response


if __name__ == "__main__":
    client = ImageAnalysisClient()
    image_url = "https://learn.microsoft.com/azure/cognitive-services/computer-vision/images/windows-kitchen.jpg"
    features = ["caption", "tags", "denseCaptions", "objects"]
    response = client.image_analysis(image=image_url, features = features)
    print(response)