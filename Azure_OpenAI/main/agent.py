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
        self.API_OPENAI_ENDPOINT = os.getenv("API_OPENAI_ENDPOINT")
        self.API_OPENAI_KEY = os.getenv("API_OPENAI_KEY")

        # speech-to-text credentials
        self.API_SPEECH_TO_TEXT_ENDPOINT = os.getenv("API_SPEECH_TO_TEXT_ENDPOINT")
        self.API_SPEECH_TO_TEXT_KEY = os.getenv("API_SPEECH_TO_TEXT_KEY")

        # Text-to-speech credentials
        self.API_TEXT_TO_SPEECH_ENDPOINT = os.getenv("API_TEXT_TO_SPEECH_ENDPOINT")
        self.API_TEXT_TO_SPEECH_KEY = os.getenv("API_TEXT_TO_SPEECH_KEY")