import os
import requests
from dotenv import load_dotenv

class Agent():

    def __init__(self):

        load_dotenv()

        self.API_DOCUMENT_INTELLIGENCE_ENDPOINT = os.getenv("API_DOCUMENT_INTELLIGENCE_ENDPOINT")
        self.API_DOCUMENT_INTELLIGENCE_KEY = os.getenv("API_DOCUMENT_INTELLIGENCE_KEY")

    def document_intelligence():
        return
    
if __name__ == "__main__":
    agent = Agent()
    