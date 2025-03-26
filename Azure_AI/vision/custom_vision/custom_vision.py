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

        self.trainer = None
        self.predictor = None

        # Authenticate internally upon class object creation.
        self.authenticate()

    
    # Instantiate a training and prediction client with authentication credentials
    def authenticate(self):
        """
        Authenticate and set up the trainer and predictor.
        This method can be called explicitly to re-authenticate if needed.
        """
        training_credentials = ApiKeyCredentials(in_headers={"Training-key": self.API_CUSTOM_VISION_TRAINING_KEY})
        self.trainer = CustomVisionTrainingClient(endpoint = self.API_CUSTOM_VISION_TRAINING_ENDPOINT, credentials = training_credentials)

        prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": self.API_CUSTOM_VISION_PREDICTION_KEY})
        self.predictor = CustomVisionPredictionClient(endpoint = self.API_CUSTOM_VISION_PREDICTION_ENDPOINT, credentials = prediction_credentials)

    
    def get_project(self):

        # get project model
        for project in self.trainer.get_projects():
            print("PROJECT: {} - {}".format(project.name, project.id))

        # get project domain
        for domain in self.trainer.get_domains():                            # list of available domains
            print("DOMAIN: {} - {}".format(domain.name, domain.id))     # information about each domain


    # Create a new Custom Vision project
    def set_project(self, project_name, project_description):

        project_id, domain_id = self.validate_project(project_name)

        if domain_id:

            # If project with the same project name already exists, retrieve the existing project information.
            if project_id:
                project = self.trainer.get_project(project_id = project_id)

            # Create a new project by configuring project name, project description, and a domain.
            else:
                project = self.trainer.create_project(project_name, project_description, domain_id)

        return project.id

    
    def validate_project(self, project_name):

        project_id, domain_id = "", ""

        for project in self.trainer.get_projects():
            if project.name == project_name:
                project_id = project.id
                break
        
        for domain in self.trainer.get_domains():
            if domain.type == "ObjectDetection" and domain.name == "General (compact)":
                domain_id = domain.id
                break

        return project_id, domain_id


    def get_tags(self, project_name):
        project_id = self.validate_project(project_name)[0]

        tag_list = self.trainer.get_tags(project_id = project_id)
        
        return tag_list
    

    def validate_tags(self, project_name, *tags):
        # TODO: implementations for general cases
        """
        tags = dict()

        for tag in tags:
            tags.update(
                {
                    f"tag": None
                }
            )

        """
        project_id = self.validate_project(project_name)[0]
        existing_tags = self.get_tags(project_name)

        fork_tag = None
        scissors_tag = None

        for tag in existing_tags:
            if tag.name == "fork":
                print("The tag 'fork' already existing in this project.")
                fork_tag = tag
            elif tag.name == "scissors":
                print("The tag 'scissors' already exsting in this project.")
                scissors_tag = tag

        if fork_tag is None:
            print("Creating new tag: 'fork'")
            fork_tag = self.trainer.create_tag(project_id = project_id, name = "fork")
        
        if scissors_tag is None:
            print("Creating new tag 'scissors'")
            scissors_tag = self.trainer.create_tag(project_id = project_id, name = "scissors")

        return fork_tag.id, scissors_tag.id


if __name__ == "__main__":
    client = CustomVisionClient()
    client.get_project()

    # Project Creation
    project_name = "6a009-objectDetection-model"
    project_description = "Custom Vision Object Detection Project"
    project_id = client.set_project(project_name = project_name, project_description = project_description)
    print(project_name, project_id)
    
    client.get_tags(project_name)
    client.validate_tags(project_name, ())