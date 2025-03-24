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

        # gpt-4o-mini credentials
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
                            "text": "You are an AI assistant that helps people find information."
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
            return f"Error {response.status_code}: {response.reason}"


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
            #return f"Error {response.status_code}: {response.reason}"
            print(f"Error {response.status_code}: {response.reason}")
            return None

    def text_to_speech(self, text):

        headers = {
            "Ocp-Apim-Subscription-Key": self.API_TEXT_TO_SPEECH_KEY,
            "Content-Type": "application/ssml+xml",
            "X-Microsoft-OutputFormat": "riff-24khz-16bit-mono-pcm"
        }

        body = f"""
        <speak version='1.0' xml:lang='en-US'>
            <voice name='en-US-AvaMultilingualNeural'>
                <prosody rate='0%'>
                    {text}
                </prosody>
            </voice>
        </speak>
        """

        response = requests.post(self.API_TEXT_TO_SPEECH_ENDPOINT, headers = headers, data = body)

        if response.status_code == 200:
            file_path = "Azure_OpenAI/speech/response_audio.wav"
            with open(file_path, "wb") as audio_file:
                audio_file.write(response.content)
            return file_path
        
        else:
            return f"Error {response.status_code}: {response.reason}"
    

if __name__ == "__main__":
    agent = Agent()

    responses = {
        "gpt-4o-mini": agent.gpt_4o_mini("Hello"),
        "speech-to-text": agent.speech_to_text("Azure_OpenAI/speech/audio1.wav"),
        "text-to-speech": agent.text_to_speech("Hello")
    }

    print(responses)