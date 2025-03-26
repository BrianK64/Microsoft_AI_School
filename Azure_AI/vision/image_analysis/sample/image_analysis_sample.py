from dotenv import load_dotenv
import os
import requests
import gradio as gr
from PIL import Image, ImageDraw, ImageFont
import random
import platform


load_dotenv()

ENDPOINT = os.getenv("API_VISION_ENDPOINT")
API_KEY = os.getenv("API_VISION_KEY")
API_VERSION = os.getenv("API_VISION_VERSION")

FEATURES = ["read", "smartCrops", "tags", "people", "caption", "denseCaptions", "objects"]


def request_vision(features, image_path, language, smart_crops = ""):

    endpoint = f"{ENDPOINT}computervision/imageanalysis:analyze"

    query_params = {
        "api-version": API_VERSION,
        "features": ",".join(features),
        "languague": language
    }

    if "smartCrops" in features:
        query_params.update({
            "smartcrops-aspect-ratios": smart_crops
        })

    # method
    headers = {
        "Ocp-Apim-Subscription-Key": API_KEY,
        "Content-Type": "application/octet-stream"
    }

    # Read image as a binary data
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    response = requests.post(endpoint, params= query_params, headers = headers, data = image_data)
    print(response.text)
    if response.status_code == 200:
        return response.json()
    else:
        return {}
    

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def get_font():
    font_size = 50
    if platform.system() == "Darwin":
        font = ImageFont.truetype("AppleGothic.ttf", size = font_size)
    elif platform.system() == "Windows":
        font = ImageFont.truetype("malgun.ttf", size = font_size)
    else:
        font = ImageFont.load_default(size = font_size)

    return font


def draw_image(image_path, features, response_json):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = get_font()

    for feature in features:
        result_object = response_json["{}Result".format(feature)]
        color = random_color()

        if "values" in result_object.keys():
            block_list = result_object["values"]

            for block in block_list:
                bounding_box = block.get("boundingBox", None)
                confidence = block.get("confidence", 1)

                if bounding_box and confidence > 0.80:
                    x, y, w, h = bounding_box["x"], bounding_box["y"], bounding_box["w"], bounding_box["h"]

                    draw.rectangle([(x, y), (x + w, y + h)], outline = color, width = 5)
                    draw.text((x + 10, y + 10), text = feature, fill = color, font = font)

    return image


with gr.Blocks() as demo:

    def change_image(image_path, features, language, smart_crops):

        if image_path:
            response_json = request_vision(features, image_path, language, smart_crops)
            image = draw_image(image_path, features, response_json)
            return image, response_json
        else:
            return None, None
        
    
    def change_features(features):
        print(features)
        if "smartCrops" in features:
            return features, gr.update(visible = True)
        else:
            return features, gr.update(visible = False)
        

    def change_language(language, features):
        print(language)
        print(set(features), features)

        value = list(set(FEATURES[:4]) & set(features))
        if language == "ko":
            return language, gr.update(choices = FEATURES[:4], value = value)
        else:
            return language, gr.update(choices = FEATURES, value = value)
        


    # Select language, features, smartcrops aspect ratios
    with gr.Column():
        language_radio = gr.Radio(label = "Select language", choices = ["en", "ko"], value = "en")
        features_checkbox = gr.CheckboxGroup(label = "Features", choices = FEATURES)
        smart_crops_textbox = gr.Textbox(label = "Smart Crops", visible = False)


    # input image
    with gr.Column():
        input_image = gr.Image(label = "Input image", type = "filepath", height = 400)
        send_button = gr.Button("Send")

    
    # output image and JSON response
    with gr.Row():
        output_image = gr.Image(label = "Output image", type = "pil", interactive = False)
        output_json = gr.JSON(label = "Result JSON")


    # Eveng handling
    input_image.change(change_image, inputs = [input_image, features_checkbox, language_radio, smart_crops_textbox], outputs = [output_image, output_json])
    send_button.click(change_image, inputs = [input_image, features_checkbox, language_radio, smart_crops_textbox], outputs = [output_image, output_json])
    language_radio.change(change_language, inputs = [language_radio, features_checkbox], outputs = [language_radio, features_checkbox])
    features_checkbox.change(change_features, inputs = [features_checkbox], outputs = [features_checkbox, smart_crops_textbox])


demo.launch()