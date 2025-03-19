import gradio as gr
from PIL import Image, ImageDraw
import random
from agent import Agent

def main():
    agent = Agent()

    def random_color():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


    def draw_image(file_path, result_response):
        image = Image.open(file_path)
        draw = ImageDraw.Draw(image)

        block_list = result_response["analyzeResult"]["paragraphs"]

        for block in block_list:
            line_color = random_color()
            polygon_list = block["boundingRegions"][0]["polygon"]
            points = [[polygon_list[i], polygon_list[i + 1]] for i in range(0, len(polygon_list), 2)]
            content = block["content"]

            draw.polygon(points, outline = line_color, width = 2)
            draw.text((points[0][0], points[0][1] - 10), content, fill = line_color)

        return image
    
    
    with gr.Blocks() as page_main:

        def click_submit(file_path):
            result_response = agent.document_intelligence(file_path)["json"]
            image = draw_image(file_path, result_response)
            return image


        input_image = gr.Image(label = "Input Image", type = "filepath")
        submit_button = gr.Button("Submit")
        output_image = gr.Image(label = "Output Image", interactive = False, type = "pil")

        submit_button.click(click_submit, inputs = [input_image], outputs = [output_image])

    page_main.launch()

if __name__ == "__main__":
    main()