import gradio as gr
from agent import Agent

def main():
    agent = Agent()
    with gr.Blocks() as page_main:
        gr.Markdown("# Azure AI Speech Service")

        def gpt_click(prompt, history):
            return

        def update_audio_source(audio_path):
            if audio_path:
                text = agent.speech_to_text(audio_path)
                return text
            else:
                return None
        
        def tts_click(text):
            return

        with gr.Row():

            # gpt-4o mini language model
            with gr.Column():
                chatbot = gr.Chatbot(type = "messages")
                with gr.Row():
                    prompt = gr.Textbox(label = "Prompt", scale = 6)
                    gpt_button = gr.Button("^", scale = 1)

                gpt_audio = gr.Audio(interactive = False, autoplay = True)
                gpt_button.click(gpt_click, inputs = [prompt, chatbot], outputs = [prompt, chatbot])

            with gr.Column(scale = 1):
                # Speech-to-Text model
                with gr.Column():
                    gr.Markdown("## Speech to Text")

                    input_mic = gr.Audio(label="Mic", sources = "microphone", type = "filepath", show_download_button = True)
                    transcription_textbox = gr.Textbox(label = "Transcribed Text", interactive = False)
                    input_mic.change(update_audio_source, inputs = [input_mic], outputs = [transcription_textbox])

                # Text-to-Speech model
                with gr.Column():
                    gr.Markdown("## Text to Speech")

                    tts_textbox = gr.Textbox(label = "Text", placeholder = "Enter the text you want to convert into speech")    # input
                    tts_voice = gr.Dropdown(label = "Voice", choices = ["en-US-AvaMultilingualNeural", "en-US-EmmaMultilingualNeural", "en-US-EchoTurboMultilingualNeural", "en-US-BrianMultilingualNeural"], interactive = True)
                    tts_button = gr.Button("Convert")   # conversion
                    tts_audio = gr.Audio(interactive = False, autoplay = True) # output

                    tts_button.click(fn = tts_click, inputs = [tts_textbox], outputs = [tts_audio])


    page_main.launch()


if __name__ == "__main__":
    main()