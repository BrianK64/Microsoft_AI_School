import gradio as gr
from image_analysis import ImageAnalysisClient
from PIL import Image, ImageDraw

def draw_image(image_path):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    return Image

def main():

    client = ImageAnalysisClient()

    with gr.Blocks as main:

        def change_image(image_path, *features):

            if image_path:
                response_json = client.image_analysis(image_path, features)
                image = draw_image(image_path)
                return image, response_json
            
            else:
                return None, None
            

        # Image Analysis Configuration Interactions
        with gr.Column():
            language_radio = gr.Radio(label = "Select Language", choices = ["en", "ko"], value = "en")
            features_checkbox = gr.CheckboxGroup(label = "Image Analysis Features", choices = ["1", "2"])
            smart_crops_texxtbox = gr.Textbox(label = "Smart Crops")

        
        # User Input Image
        with gr.Column():
            input_image = gr.Image(label = "Image to analyze", type = "filepath", height = 400)


        with gr.Row():
            output_image = gr.Image(label = "Image Analysis", type = "pil", interactive = False)
            output_json = gr.JSON(label = "Analysis results JSON file",)