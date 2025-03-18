import gradio as gr

def main():
    with gr.Blocks() as page_main:
        gr.Markdown("# Azure AI Speech Service")

        def update_audio_source(audio_path):
            return audio_path

        with gr.Column():
            gr.Markdown("## Speech to Text")

            input_mic = gr.Audio(label="Mic", sources = "microphone", type = "filepath", show_download_button = True)
            transcription_textbox = gr.Textbox(label = "Transcribed Text", interactive = False)
            input_mic.change(update_audio_source, inputs = [input_mic], outputs = [transcription_textbox])

    page_main.launch()


if __name__ == "__main__":
    main()