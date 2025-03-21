import gradio as gr
from agent import Agent
import re

def main():

    agent = Agent()

    with gr.Blocks() as demo:
        
        def change_audio(audio_path):
            if audio_path:
                text = (audio_path)
                return text
            else:
                return ""
            
        def click_send(text):
            file_path = agent.speech_to_text(text)
            if file_path:
                return file_path
            else:
                return None
        
        def click_gpt_send(prompt, histories):
            content = agent.gpt_4o_mini(prompt)
            histories.append({"role": "user", "content": prompt})
            if content:    
                histories.append({"role": "assistant", "content": content})
            else:
                error_message = "응답을 받지 못했습니다."
                histories.append({"role": "assistant", "content": error_message})
            
            return "", histories
        
        def change_chatbot(histories):
            return
            history = histories[-1]
            content = history['content']
            pattern = r'[^가-힣a-zA-Z0-9\s]'
            cleaned_content = re.sub(pattern, '', content)
            audio_path = request_tts(cleaned_content)
            
            return audio_path
            
        gr.Markdown("# AI Speech World!! #")
        with gr.Row():
            
            # 좌측
            with gr.Column(scale=4):
                chatbot = gr.Chatbot(type="messages")
                with gr.Row():
                    prompt = gr.Textbox(label="프롬프트", scale=6)
                    send_gpt_button = gr.Button("전송", scale=1)
                
                gpt_audio = gr.Audio(interactive=False, autoplay=True)
            
            # 우측
            with gr.Column(scale=1):
                # STT
                with gr.Column():
                    gr.Markdown("### STT ###")
                    
                    input_mic = gr.Audio(label="마이크 입력", sources="microphone", type="filepath", 
                                        show_download_button=True)
                    output_textbox = gr.Textbox(label="텍스트", interactive=False)
                
                # TTS    
                with gr.Column():
                    gr.Markdown("### TTS ###")
                    
                    tts_textbox = gr.Textbox(label="입력", placeholder="음성 변환할 텍스트를 입력하세요.")
                    send_tts_button = gr.Button('전송')        
                    output_tts_audio = gr.Audio(interactive=False, autoplay=True) 
                    
        send_tts_button.click(fn=click_send, inputs=[tts_textbox], outputs=[output_tts_audio])
        send_gpt_button.click(click_gpt_send, inputs=[prompt, chatbot], outputs=[prompt, chatbot])
        input_mic.change(change_audio, inputs=[input_mic], outputs=[prompt])
        chatbot.change(change_chatbot, inputs=[chatbot], outputs=[gpt_audio])
            
            
    demo.launch()


if __name__ == "__main__":
    main()