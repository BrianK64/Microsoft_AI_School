import gradio as gr
from agent import Agent

with gr.Blocks() as demo:

    # Handle user input prompt and update the chat history
    def click_submit(prompt, history):
        # GPT-4o mini request
        content, references = Agent(prompt= prompt)

        # new agent-user interaction
        chat = [
            {
                "role": "user",
                "content": prompt
            },
            {
                "role": "assistant",
                "content": content
            }
        ]
        # update the history with new interactions
        history.extend((chat))
        return history, references, "" # clear the prompt textbox after submission
    

    gr.Markdown("# 🎬NETFLIX Recommendation Engine🍿")

    with gr.Group():
        with gr.Column():
            # Initial greeting message from the agent
            greeting = [
                {
                    "role": "assistant",
                    "content": "Hey there! Ready to find your next binge-worthy show or movie? 🎥✨ Tell me what you're in the mood for—thrilling action, heartwarming romance, laugh-out-loud comedy, or something totally unexpected! I’ve got some awesome recommendations just for you. Let’s dive in! 🚀🔥"
                }
            ]

            # chatbot instance that starts with the greeting message
            chatbot = gr.Chatbot(greeting, label = "GPT-4o mini", type = "messages")
            reference_textbox = gr.Textbox(label = "Reference")

    with gr.Group():
        with gr.Row():
            prompt_textbox = gr.Textbox(label = "Prompt", placeholder = "Ask anything", scale = 6)
            submit_button = gr.Button("^", scale = 2)

    # button behavior definition
    submit_button.click(click_submit, inputs = [prompt_textbox, chatbot], outputs = [chatbot, reference_textbox, prompt_textbox])

demo.launch()