import os
from dotenv import load_dotenv
import requests
from IPython.display import Markdown

load_dotenv()

API_ENDPOINT = os.getenv("API_ENDPOINT")
API_KEY = os.getenv("API_KEY")

AI_SEARCH_ENDPOINT = os.getenv("AI_SEARCH_ENDPOINT")
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
                "content": "You are an AI travel assistant specializing in helping travelers and visitors plan their trips to Namhae, South Korea. Your audience communicates in Korean, so you will primarily receive questions in Korean and are expected to respond in Korean."
            },
            ### few-shot learning
            # {
            #     "role": "user",
            #     "content": "남해 여행지 3곳 추천해줘"
            # },
            # {
            #     "role": "assistant",
            #     "content": "남해에서 추천할 만한 여행지 3곳은 다음과 같습니다:\n\n1. **남해 지족도**: 이곳은 아름다운 해변과 수려한 자연경관으로 유명합니다. 특히, 해안선을 따라 조성된 산책로가 있어 여유로운 산책을 즐기기 좋은 장소입니다 .\n\n2. **남해 독일마을**: 독일 이민자들이 살던 마을로, 독일식 건축물과 음식이 매력적입니다. 이곳에서 독일 맥주와 소시지를 맛보며 독특한 경험을 할 수 있습니다 .\n\n3. **남해 상주은모래비치**: 맑고 푸른 바다와 고운 모래사장이 인상적인 해수욕장입니다. 여름철에는 많은 관광객이 찾는 인기 있는 장소로, 다양한 수상 스포츠를 즐길 수 있습니다 .\n\n이 외에도 남해는 다양한 관광명소와 아름다운 자연이 많이 있으니, 여행 계획에 참고하시기 바랍니다!"
            # },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7,
        "top_p": 0.95,
        "max_tokens": 800,
        "data_sources": [
            {
                "type": "azure_search",
                "parameters": {
                    "endpoint": AI_SEARCH_ENDPOINT,
                    "index_name": AI_SEARCH_INDEX,
                    "semantic_configuration": "default",
                    "query_type": "simple",
                    "fields_mapping": {},
                    "in_scope": True,
                    #"role_information": "You are an AI assistant that helps people find information.",
                    "filter": None,
                    "strictness": 3,
                    "top_n_documents": 5,
                    "authentication": {
                        "type": "api_key",
                        "key": AI_SEARCH_API_KEY
                    },
                    "key": AI_SEARCH_API_KEY
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
        #content_md = display(Markdown(content))

        content = content + "\n\nReferences\n\n"
        for i, ref in enumerate(references):
            content = content + f"{i+1}. {ref}\n\n"
        
        
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
    prompt = "일주일 남해 여행 스케줄 만들어줘"
    print(search(prompt))
    
    # if search(prompt):
    #     print("AI response has been saved as a markdown file in the current working dirrectory.")
    # else:
    #     print(search(prompt).status_code, search(prompt).reason)