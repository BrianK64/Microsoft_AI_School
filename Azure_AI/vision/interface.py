import gradio as gr
from image_analysis import ImageAnalysisClient
from PIL import Image, ImageDraw

def draw_image(image_path):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    return Image

FEATURES = ["read", "caption", "denseCaptions", "smartCrops", "objects", "tags", "people"]

def main():

    client = ImageAnalysisClient()

    with gr.Blocks() as main:

        def change_image(image_path, features, language, smartcrops_aspect_ratios):

            if image_path:
                response_json = client.image_analysis(image = image_path, features = features, language = language, smartcrops_aspect_ratios = smartcrops_aspect_ratios)
                image = draw_image(image_path)
                return image, response_json
            
            else:
                return None, None
            
        
        def change_features(features):
            print(features)
            
            if "smartCrops" in features:
                return features, gr.update(visible = True)
            
            else:
                return features, gr.update(visible = False)
            
        
        def change_language(language):
            print(language)

            if language == "ko":
                return language, gr.update(choices = FEATURES[:4], value = [])
            
            else:
                return language, gr.update(choices = FEATURES, value = [])
            

        # Image Analysis Configuration Selections
        with gr.Column():
            language_radio = gr.Radio(label = "Select Language", choices = ["en", "ko"], value = "en")
            features_checkbox = gr.CheckboxGroup(label = "Image Analysis Features", choices = FEATURES)
            smartcrops_aspect_ratios_textbox = gr.Textbox(label = "Select smart croppping aspect ratios", visible = False)

        
        # User Input Image
        with gr.Column():
            input_image = gr.Image(label = "Image to analyze", type = "filepath", height = 400)


        with gr.Row():
            output_image = gr.Image(label = "Image Analysis", type = "pil", interactive = False)
            output_json = gr.JSON(label = "Analysis results JSON file")

        
        # Event Handling
        input_image.change(fn = change_image, inputs = [input_image, features_checkbox, language_radio, smartcrops_aspect_ratios_textbox], outputs = [output_image, output_json])

        language_radio.change(fn = change_language, inputs = [language_radio], outputs = [language_radio, features_checkbox])

        features_checkbox.change(fn = change_features, inputs = [features_checkbox], outputs = [features_checkbox, smartcrops_aspect_ratios_textbox])

    
    return main


if __name__ == "__main__":
    main().launch()