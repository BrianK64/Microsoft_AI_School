import os
import requests
from dotenv import load_dotenv
import uuid

class Agent():

    def __init__(self):

        load_dotenv()

        self.API_LANGUAGE_ENDPINT = os.getenv("API_LANGUAGE_ENDPOINT")
        self.API_LANGUAGE_KEY = os.getenv("API_LANGUAGE_KEY")
        self.headers = {
            "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": self.API_LANGUAGE_KEY
        }


    def named_entity_recognition(self, language="en", text = "This is a sample text."):
        
        request_id = str(uuid.uuid4())
        
        body = {
            "kind": "EntityRecognition",
            "parameters": {
                "modelVersion": "latest"
            },
            "analysisInput":{
                "documents":[
                    {
                        "id": request_id,
                        "language":language,
                        "text": text
                    }
                ]
            }
        }

        response = requests.post(self.API_LANGUAGE_ENDPINT, headers = self.headers, json = body)

        if response.status_code == 200:
            response_json = response.json()
            return response_json
        
        else:
            print(f"error {response.status_code}: {response.reason}")
            return None
        

    def PII_detection(self, language="en", text="This is a sample text"):   # Personally Identifiable Information (PII) detection

        request_id = str(uuid.uuid4())

        body = {
            "kind": "PiiEntityRecognition",
            "parameters": {
                "modelVersion": "latest"
            },
            "analysisInput":{
                "documents":[
                    {
                        "id": request_id,
                        "language":language,
                        "text": text
                    }
                ]
            }
        }

        response = requests.post(self.API_LANGUAGE_ENDPINT, headers = self.headers, json = body)

        if response.status_code == 200:
            response_json = response.json()
            return response_json
        
        else:
            print(f"error {response.status_code}: {response.reason}")
            return None
        

if __name__ == "__main__":
    agent = Agent()
    NER_text = "Named Entity Recognition (NER) is one of the features offered by Azure AI Language, a collection of machine learning and AI algorithms in the cloud for developing intelligent applications that involve written language. The NER feature can identify and categorize entities in unstructured text. For example: people, places, organizations, and quantities. The prebuilt NER feature has a preset list of recognized entities. The custom NER feature allows you to train the model to recognize specialized entities specific to your use case."
    
    NER_response = agent.named_entity_recognition(text = NER_text)
    entities = NER_response["results"]["documents"][0]["entities"]
    print("Named Entities:\n")
    for entity in entities:
        print(f"""\tText:\t{entity["text"]}\tCategory:\t{entity["category"]}\tSubCategory:\t{entity.get("subcategory", "None")}\n\tConfidence Score:\t{round(entity["confidenceScore"], 2)}\tLength:\t{entity["length"]}\tOffset:\t{entity["offset"]}\n""")
    
    PII_text = "Call our office at 312-555-1234, or send an email to support@contoso.com"
    PII_response = agent.PII_detection(text = PII_text)
    print("\n", PII_response)