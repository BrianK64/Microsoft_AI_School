# Imports
import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_ENDPOINT = os.getenv("API_ENDPOINT")
API_KEY = os.getenv("API_KEY")

AI_SEARCH_API_ENDPOINT = os.getenv("AI_SEARCH_API_ENDPOINT")
AI_SEARCH_API_KEY = os.getenv("AI_SEARCH_API_KEY")

AI_SEARCH_INDEX = os.getenv("AI_SEARCH_INDEX")
AI_SEARCH_SEMANTIC = os.getenv("AI_SEARCH_SEMANTIC")

def search(prompt):

    # endpoint
    endpoint = API_ENDPOINT

    # method: POSt

    # headers: includes key
    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY
    }

    # body: json
    body = {
        "messages": [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "You are an AI assistant providing personalized recommendations for movies and TV shows available on Netflix by analyzing the user's preferences (genres, casts, directors). Ensure responses include the description, director, cast, genre, rating, and release year to make suggestions friendly and engaging yet concise. Also make sure to cite references."
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
        "top_p": 0.95,
        "max_tokens": 800
    }

    response = requests.post(endpoint, headers = headers, json = body)
    if response.status_code == 200:
        response_json = response.json()
        message = response_json["choices"][0]["message"]
        #content_filter = response_json["choices"][0]["content_filter_results"]
        role = message["role"]
        content = message["content"]

        # citations = response_json["choices"][0]["message"]["context"]["citations"]
        # references = []
        # for citation in citations:
        #     references.append(citation["content"])
        # #content_md = display(Markdown(content))

        # content = content + "\n\nReferences\n\n"
        # for i, ref in enumerate(references):
        #     content = content + f"{i+1}. {ref}\n\n"
        
        
        # file_path = os.path.join(os.getcwd(), "Azure_OpenAI/search/response.md")
        # with open(file_path, "w", encoding = "utf-8") as file:
        #     file.write(content)
        #     file.write("\n\nReferences\n")
        #     for i, ref in enumerate(references):
        #         file.write(f"{i+1}. {ref}")

        return content
    
    else:
        return response

if __name__ == "__main__":
    prompt = "I want to watch an action movie featuring Dwayne Johnson"
    print(search(prompt))
    
    # if search(prompt):
    #     print("AI response has been saved as a markdown file in the current working dirrectory.")
    # else:
    #     print(search(prompt).status_code, search(prompt).reason)