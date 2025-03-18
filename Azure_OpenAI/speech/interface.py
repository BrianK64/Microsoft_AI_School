import gradio as gr

def main():
    with gr.Blocks() as page_main:
        gr.Markdown("# Azure AI Speech Service")

        with gr.Column():
            gr.Markdown("## Speech to Text")

            input_mic = gr.Audio(label="Mic", sources = "microphone", type = "filepath", show_download_button = True)