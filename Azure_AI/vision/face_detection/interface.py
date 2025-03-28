import gradio as gr
from face_detection import FaceDetectionClient

def main():

    client = FaceDetectionClient()

    with gr.Blocks() as main:

        def stream_webcam(image):
            detected_image = client.face_detection(image)
            return detected_image
        
        input_webcam = gr.Image(label = "Webcam", sources = "webcam", streaming = True, width = 480, height = 270, mirror_webcam = False)
        output_image = gr.Image(label = "Results", streaming = True)

        input_webcam.stream(fn = stream_webcam, inputs = [input_webcam], outputs = output_image)

    return main


if __name__ == "__main__":
    main = main()
    main.launch()