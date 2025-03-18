import gradio as gr

def main():
    with gr.Blocks() as page_main:
        gr.Markdown("# Azure AI Speech Service")

        with gr.Column():
            gr.Markdown("## Speech to Text")

            input_mic = gr.Audio(label="Mic", sources = "microphone", type = "filepath", show_download_button = True)
            output_textbox = gr.Textbox(label = "Transcribed Text", interactive = False)

    page_main.launch()


if __name__ == "__main__":
    main()