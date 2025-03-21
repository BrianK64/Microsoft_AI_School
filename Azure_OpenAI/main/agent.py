# Imports
import os
import requests
from dotenv import load_dotenv

# Azure AI Service agent
class Agent():

    def __init__(self):

        # load environmental variables
        load_dotenv()

        # Azure AI Service Authentication
        