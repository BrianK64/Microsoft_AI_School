import os
import requests
import time
from dotenv import load_dotenv

class Agent():

    def __init__(self):

        load_dotenv()

        self.API_DOCUMENT_INTELLIGENCE_ENDPOINT = os.getenv("API_DOCUMENT_INTELLIGENCE_ENDPOINT")
        self.API_DOCUMENT_INTELLIGENCE_KEY = os.getenv("API_DOCUMENT_INTELLIGENCE_KEY")
        self.headers = {
            "Ocp-Apim-Subscription-Key": self.API_DOCUMENT_INTELLIGENCE_KEY,
            "Content-Type":"image/*"
        }

    def document_intelligence(self, file_path):
        with open(file_path, "rb") as image:
            image_data = image.read()

        response = requests.post(self.API_DOCUMENT_INTELLIGENCE_ENDPOINT, headers = self.headers, data = image_data)

        if response.status_code == 202:
            result_url = response.headers["Operation-Location"]

            while (True):
                result_response = requests.get(result_url, headers = {
                    "Ocp-Apim-Subscription-Key": self.headers["Ocp-Apim-Subscription-Key"]
                })
                result_response_json = result_response.json()
                result_status = result_response_json["status"]

                if result_status == "running":
                    print(result_status)
                    time.sleep(1)
                    continue
                else:
                    break
            
            if result_status == "succeeded":
                return {
                    "status": result_status,
                    "json": result_response_json
                    }
        
            else:
                print(f"error {response.status_code}: {response.reason}")
                return None
    
if __name__ == "__main__":
    agent = Agent()
    print(agent.document_intelligence("Azure_OpenAI/document_intelligence/sample.png"))
    