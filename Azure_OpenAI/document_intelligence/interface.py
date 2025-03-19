import gradio as gr

def main():
    with gr.Blocks() as page_main:

        input_image = gr.Image(label = "Input Image", type = "filepath")
        submit_button = gr.Button("^")
        output_image = gr.Image(label = "Output Image", interactive = False)

    page_main.launch()

if __name__ == "__main__":
    main()