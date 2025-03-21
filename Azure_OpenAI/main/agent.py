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


    def gpt_4o_mini(self, prompt):
        
        headers = {
            "Content-Type": "application/json",
            "api-key": self.API_OPENAI_KEY
        }

        body = {
            "messages": [
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "text",
                            "text": "You are Jarvis, an AI assistant that helps people find information, perform daily tasks, and provide insights. You will always answer in a very professional and formal tone, and always greet the user with 'Hello, sir'"
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ],
            "temperature": 0.7,
            "top_p": 0.9,
            "max_tokens": 2000
        }

        response = requests.post(self.API_OPENAI_ENDPOINT, headers = headers, json = body)

        if response.status_code == 200:
            response_json = response.json()
            message = response_json["choices"][0]["message"]
            role = message["role"]
            content = message["content"]
            return content
        
        else:
            print(f"Error {response.status_code}: {response.reason}")
            return None
        
    
    def speech_to_text(self, audio_path, to_lang="en-US"):


        headers = {
            "Ocp-Apim-Subscription-Key": self.API_SPEECH_TO_TEXT_KEY,
            "Content-Type": "audio/wav"
        }

        with open(audio_path, "rb") as audio:
            audio_data = audio.read()

        response = requests.post(self.API_SPEECH_TO_TEXT_ENDPOINT, headers=headers, data=audio_data)
        if response.status_code == 200:

            response_json = response.json()
            text = response_json["DisplayText"]
            return text
        
        else:
            print(f"Error {response.status_code}: {response.reason}")
            return None
        

if __name__ == "__main__":
    agent = Agent()
    prompt = "Hi Jarvis"
    response = agent.gpt_4o_mini(prompt = prompt)
    print(response)