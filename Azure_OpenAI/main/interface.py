import gradio as gr
from agent import Agent


agent = Agent()


def activate():
    return gr.update(visible=True), gr.update(visible=False)


def set_audio(audio_path):
    if audio_path:
        text = agent.speech_to_text(audio_path)
        return text
    else:
        return None


def main():
    with gr.Blocks() as JARVIS:

        with gr.Column(visible = True) as deactivated:
        
            Jarvis_deactivated = gr.Image("Azure_OpenAI/main/jarvis_deactivated.jpg", interactive = True)
            activation_button = gr.Button("activate")

            activation_button.click(fn = activate, inputs = [], outputs = [])

        
        with gr.Column(visible = False) as activated:
            Jarvis_activated = gr.Image("Azure_OpenAI/main/jarvis_activated.gif", interactive = False)
            Jarvis = gr.Chatbot(label = "J.A.R.V.I.S", type = "messages", visible = False)
            
            # button: mic input, visible
            # -> textbox: text output, invisible
            # -> chatbot: text input, invisible
            # -> chatbot: text output, invisible
            # -> audio: response, invisible
            
            #query_stt_audio = gr.Audio(sources = "microphone", type = "filepath", show_download_button = False)
            #query_stt_text = gr.Textbox(visible = False)
            #query_stt_audio.change(fn = set_audio, inputs = [query_stt_audio], outputs = [query_stt_text])
            #query_tts_text = gr.Textbox()

            deactivation_button = gr.Button("deactivate")
            

        activation_button.click(fn = activate, inputs = [], outputs = [activated, deactivated])
        deactivation_button.click(fn = activate, inputs = [], outputs = [deactivated, activated])

    return JARVIS


if __name__ == "__main__":
    main().launch()