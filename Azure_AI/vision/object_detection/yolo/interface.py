import gradio as gr

def main():

    with gr.Blocks() as main:

        def stream_webcam(image):
            drawn_image = image
            return drawn_image
        

        def click_capture(image):
            return image
        

        with gr.Row():
            #TODO: components
            """
            webcam
            real-time object detection screen
            Capture screen
            """

            webcam_input = gr.Image(label = "Real-Time Screen", sources = "webcam", width = 480, height = 270, mirror_webcam = False)
            output_image = gr.Image(label = "검출 화면", type = "pil", interactive = False)
            output_capture_image = gr.Image(label = "캡쳐 화면", interactive = False)


        with gr.Row():
            #TODO: components
            """
            capture button
            analysis button
            """

            capture_button = gr.Button("Screen capture")
            send_gpt_button = gr.Button("GPT")


        with gr.Column():
            #TODO: components
            """
            chatbot
            TTS audio to read GPT analysis results
            """
            chatbot = gr.Chatbot(label = "Analysis results", type = "messages")
            chtbot_audio = gr.Audio(label = "GPT", interactive = False, autoplay = True)

        
        webcam_input.stream(fn = stream_webcam, inputs = [webcam_input], outputs = [output_image])
        capture_button.click(fn = click_capture, inputs = [output_image], outputs = output_capture_image)