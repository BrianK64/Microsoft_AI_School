# Imports
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
from dotenv import load_dotenv
import os, time, uuid


# Custom Vision
class CustomVisionClient():

    def __init__(self):
        
        # load environment variables
        load_dotenv()

        # set up custom vision authentication credentials
        self.API_CUSTOM_VISION_TRAINING_ENDPOINT = os.getenv("API_CUSTOM_VISION_TRAINING_ENDPOINT")
        self.API_CUSTOM_VISION_TRAINING_KEY = os.getenv("API_CUSTOM_VISION_TRAINING_KEY")
        self.API_CUSTOM_VISION_PREDICTION_ENDPOINT = os.getenv("API_CUSTOM_VISION_PREDICTION_ENDPOINT")
        self.API_CUSTOM_VISION_PREDICTION_KEY = os.getenv("API_CUSTOM_VISION_PREDICTION_KEY")
        self.API_CUSTOM_VISION_PREDICTION_RESOURCE_ID = os.getenv("API_CUSTOM_VISION_PREDICTION_RESOURCE_ID")

    
    # Instantiate a training and prediction client with authentication credentials
    def authenticate(self):
        training_credentials = ApiKeyCredentials(in_headers={"Training-key": self.API_CUSTOM_VISION_TRAINING_KEY})
        trainer = CustomVisionTrainingClient(endpoint = self.API_CUSTOM_VISION_TRAINING_ENDPOINT, credentials = training_credentials)
        prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": self.API_CUSTOM_VISION_PREDICTION_KEY})
        predictor = CustomVisionPredictionClient(endpoint = self.API_CUSTOM_VISION_PREDICTION_ENDPOINT, credentials = prediction_credentials)

        return trainer, predictor

    
    def get_project(self):
        trainer, predictor = self.authenticate()

        # get project model
        for project in trainer.get_projects():
            print("PROJECT: {} - {}".format(project.name, project.id))

        # get project domain
        for domain in trainer.get_domains():                            # list of available domains
            print("DOMAIN: {} - {}".format(domain.name, domain.id))     # information about each domain


if __name__ == "__main__":
    client = CustomVisionClient()
    client.get_project()