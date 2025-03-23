import gradio as gr
from datetime import datetime
import random
import time
from agent import Agent


agent = Agent()


def toggle():
    return gr.update(visible=True), gr.update(visible=False)


def load2():
    time.sleep(18)
    return gr.update(visible=True), gr.update(visible=False)


def get_greeting():
    current_time = datetime.now()

    if current_time.hour < 12 and current_time.hour > 6:
        message = "Good morning, Sir"

    elif current_time.hour >= 12 and current_time.hour < 18:
        message = "Good afternoon, Sir"

    else:
        message = "Good evening, Sir"

    greeting_content = random.choice([message, "Welcome back, Sir", "I am Jarvis, a virtual artificial intelligence, and I'm here to assist you with a variety of tasks as best as I can, 24 hours a day, 7 days a week. Importing all Preferences from home interface. Systems are now fully operational."])
    greeting_content = "I am Jarvis, a virtual artificial intelligence, and I'm here to assist you with a variety of tasks as best as I can. 24 hours a day, 7 days a week. Importing all Preferences from home interface. Systems are now fully operational."
    return greeting_content


def activate():
    return gr.update(visible = True)


def deactivate():
    return gr.update(visible = False)


def set_audio(audio_path):
    if audio_path:
        text = agent.speech_to_text(audio_path)
        return text
    else:
        return None
    

def get_audio(text):
    if text:
        audio_response = agent.text_to_speech(text = text)
        return audio_response
    else:
        return None
    

def get_response(prompt, chat_history):

    response = agent.gpt_4o_mini(prompt = prompt)

    chat_history.extend([
        {
            "role": "user",
            "content": prompt
        },
        {
            "role": "assistant",
            "content": response
        }
    ])

    return chat_history, response, ""


def main():
    with gr.Blocks() as JARVIS:

        with gr.Column(visible = True) as deactivated:
        
            Jarvis_deactivated = gr.Image("Azure_OpenAI/main/jarvis_deactivated.jpg", interactive = True)
            activation_button = gr.Button("activate")

        with gr.Column(visible = False) as loading:
            Jarvis_loading = gr.Image("Azure_OpenAI/main/jarvis_loading1.gif", interactive = False)
            greeting_textbox = gr.Textbox(label = "greeting", interactive = False, visible = False)
            tts_audio = gr.Audio(interactive = False, autoplay = True, visible = False)
        
        with gr.Column(visible = False) as activated:

            Jarvis_activated = gr.Image("Azure_OpenAI/main/jarvis_activated.gif", interactive = False)
            #greeting_textbox = gr.Textbox(label = "greeting", interactive = False)
            #tts_audio = gr.Audio(interactive = False, autoplay = True, visible = True)
            Jarvis = gr.Chatbot(label = "J.A.R.V.I.S", type = "messages", visible = True)
            prompt_textbox = gr.Textbox(label="Prompt")
            response_textbox = gr.Textbox(label = "Response as a text", interactive = False, visible = True)
            response_audio = gr.Audio(interactive = False, autoplay = True, visible = True)
            
            with gr.Row():
                # button: mic input, visible
                query_button = gr.Button("🔊")

            stt_audio = gr.Audio(sources = "microphone", type = "filepath", show_download_button = False, visible = False)
            #stt_response = gr.Textbox(interactive = False, visible = True)
            
            deactivation_button = gr.Button("deactivate")
            

        # J.A.R.V.I.S speech processing
        query_button.click(fn = activate, inputs = [], outputs = [stt_audio]) #js="""() => {const audioComp = document.querySelector('input[type="file"]'); if (audioComp) { audioComp.click(); } }""")
        stt_audio.change(fn = set_audio, inputs = [stt_audio], outputs = [prompt_textbox]).then(fn = deactivate, inputs = [], outputs = [stt_audio]).then(fn = get_response, inputs = [prompt_textbox, Jarvis], outputs = [Jarvis, response_textbox, prompt_textbox]).then(fn = get_audio, inputs = [response_textbox], outputs = [tts_audio])#.then(fn = set_audio, inputs = [], outputs = [stt_audio])

        # J.A.R.V.I.S activation and deactivation
        activation_button.click(fn = toggle, inputs = [], outputs = [loading, deactivated]).then(fn = get_greeting, inputs = [], outputs = [greeting_textbox]).then(fn = get_audio, inputs = [greeting_textbox], outputs = [tts_audio]).then(fn = load2, inputs = [], outputs = [activated, loading])
        #activation_button.click(fn = toggle, inputs = [], outputs = [activated, deactivated]).then(fn = get_greeting, inputs = [], outputs = [greeting_textbox]).then(fn = get_audio, inputs = [greeting_textbox], outputs = [tts_audio])
        deactivation_button.click(fn = toggle, inputs = [], outputs = [deactivated, activated]).then(fn = set_audio, inputs = [], outputs = [tts_audio])

    return JARVIS


if __name__ == "__main__":
    main().launch()