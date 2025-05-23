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

def Agent(prompt):

    # endpoint
    endpoint = API_ENDPOINT

    # method: POST

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
                "content": "You are an AI assistant providing personalized recommendations for movies and TV shows available on Netflix by analyzing the user's preferences (genres, casts, directors). Ensure responses include the description, director, cast, genre, rating, and release year to make suggestions friendly and engaging yet concise. Also make sure to cite references."

            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7,
        "top_p": 0.95,
        "max_tokens": 2000,
        "data_sources": [
            {
                "type": "azure_search",
                "parameters": {
                    "endpoint": AI_SEARCH_API_ENDPOINT,
                    "index_name": AI_SEARCH_INDEX,
                    "semantic_configuration": "default",
                    "query_type": "simple",
                    "fields_mapping": {},
                    "in_scope": True,
                    #"role_information": "You are an AI assistant providing personalized recommendations for movies and TV shows available on Netflix by analyzing the user's preferences (genres, casts, directors). Ensure responses include the description, director, cast, genre, rating, and release year to make suggestions friendly and engaging yet concise. Also make sure to cite references.",
                    "filter": None,
                    "strictness": 3,
                    "top_n_documents": 5,
                    "authentication": {
                        "type": "api_key",
                        "key": AI_SEARCH_API_KEY
                    },
                    "key": AI_SEARCH_API_KEY,
                    #"indexName": AI_SEARCH_INDEX
                }
            }
        ]
    }

    response = requests.post(endpoint, headers = headers, json = body)
    if response.status_code == 200:
        response_json = response.json()
        message = response_json["choices"][0]["message"]
        #content_filter = response_json["choices"][0]["content_filter_results"]
        role = message["role"]
        content = message["content"]

        citations = response_json["choices"][0]["message"]["context"]["citations"]
        references = []
        for citation in citations:
            references.append(citation["content"])
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

        return content, references
    
    else:
        return response

if __name__ == "__main__":
    prompt = "I want to watch an action movie featuring Dwayne Johnson"
    content, references = Agent(prompt)
    print(content)
    for ref in references:
        print(ref)
    
    # if search(prompt):
    #     print("AI response has been saved as a markdown file in the current working dirrectory.")
    # else:
    #     print(search(prompt).status_code, search(prompt).reason)