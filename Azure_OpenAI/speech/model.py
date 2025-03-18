# Imports
import os
import requests
from dotenv import load_dotenv

# Speech Service Agent
# Supports Speech-to-Text and Text-to-Speech functionalities.
class Agent():

    def __init__(self):

        # load environment variables
        load_dotenv()

        # speech-to-text credentials
        self.API_SPEECH_TO_TEXT_ENDPOINT = os.getenv("API_SPEECH_TO_TEXT_ENDPOINT")
        self.API_SPEECH_TO_TEXT_KEY = os.getenv("API_SPEECH_TO_TEXT_KEY")

        # Text-to-speech credentials
        self.API_TEXT_TO_SPEECH_ENDPOINT = os.getenv("API_TEXT_TO_SPEECH_ENDPOINT")
        self.API_TEXT_TO_SPEECH_KEY = os.getenv("API_TEXT_TO_SPEECH_KEY")


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
            return f"Error {response.status_code}: {response.reason}"
    

    def text_to_speech(self, text):

        headers = {
            "Ocp-Apim-Subscription-Key": self.API_TEXT_TO_SPEECH_KEY,
            "Content-Type": "application/ssml+xml",
            "X-Microsoft-OutputFormat": "audio-16khz-128kbitrate-mono-mp3",
            "User-Agent": "curl"
        }
        return
    

if __name__ == "__main__":
    agent = Agent()
    response = agent.speech_to_text("Azure_OpenAI/speech/audio1.wav")
    print(response)