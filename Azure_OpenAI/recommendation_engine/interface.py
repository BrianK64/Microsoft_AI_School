import gradio as gr
from agent import Agent

# A transition function to show the next page when the video ends
def transition():
    # Return updated visibility of pages
    return gr.update(visible=True), gr.update(visible=False)

with gr.Blocks() as demo:
    # Define the introduction page (page_intro)
    with gr.Column(visible=True) as page_intro:
        video = gr.Video("Azure_OpenAI/recommendation_engine/intro.mp4.mp4", autoplay=True, show_label=False)
        transition_button = gr.Button("Start", visible = True)

    # Define the main page (page_main)
    with gr.Column(visible=False) as page_main:
        gr.Markdown("# 🎬NETFLIX Recommendation System✨")

        greeting = [
            {
                "role": "assistant",
                "content": "Hey there! Ready to find your next binge-worthy show or movie?🎥🍿 Tell me what you're in the mood for - thrilling action, heartwarming romance, laugh-out-loud comedy, or something totally unpexted!✨ I've got some awesome recommendations just for you. Let's dive in!🚀🔥"
            }
        ]

        with gr.Group():
            chatbot = gr.Chatbot(greeting, label="GPT-4o mini", type="messages")
            reference_textbox = gr.Textbox(label="Reference")
            prompt_textbox = gr.Textbox(label="Prompt", placeholder="Ask anything")

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

        prompt_textbox.submit(user_message, inputs=[prompt_textbox, chatbot], outputs=[prompt_textbox, chatbot]).then(agent_response, inputs=[chatbot], outputs=[reference_textbox, chatbot], queue=True)

    # Trigger page transition when video is done
    transition_button.click(fn=transition, inputs=[], outputs=[page_main, page_intro])

# Launch the Gradio app
demo.launch()
