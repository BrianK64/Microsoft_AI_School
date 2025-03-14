import gradio as gr

with gr.Blocks() as demo:

    gr.Markdown("# NETFLIX Recommendation Engine")
    chatbot = gr.Chatbot(label = "GPT-4o mini")

    with gr.Row():
        prompt_textboxx = gr.Textbox(label = "Prompt", placeholder = "Ask anything", scale = 6)
        submit_button = gr.Button(">", scale = 2)

demo.launch()