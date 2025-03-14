import gradio as gr
from agent import Agent
import time


with gr.Blocks() as demo:
    gr.Markdown("# 🎬NETFLIX 추천 시스템✨")

    greeting = [
        {
            "role": "assistant",
            "content": "안녕하세요! Netflix에서 영화와 시리즈를 볼 준비가 되셨나요?🎥🍿 유저의 취향과 기분에 맞게 완벽한 작품을 추천해드립니다.✨ 함께 시작해볼까요?🚀🔥"
        }
    ]

    with gr.Group():
        chatbot = gr.Chatbot(greeting, label = "GPT-4o mini", type = "messages")
        reference_textbox = gr.Textbox(label = "Reference")
        prompt_textbox = gr.Textbox(label = "Prompt", placeholder = "Ask anything")

    def user_message(prompt, chat_history):
        chat_history.extend([
            {
                "role": "user",
                "content": prompt
            }
        ])
        return "", chat_history
    
    def agent_response(chat_history):
        content, references = Agent(chat_history[-1]["content"])

        chat = [
            {
                "role": "assistant",
                "content": content
            }
        ]

        chat_history.extend(chat)

        return references, chat_history

    prompt_textbox.submit(user_message, inputs = [prompt_textbox, chatbot], outputs = [prompt_textbox, chatbot]).then(agent_response, inputs = [chatbot], outputs = [reference_textbox, chatbot], queue = True)

demo.launch()
