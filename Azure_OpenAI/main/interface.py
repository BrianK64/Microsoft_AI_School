import gradio as gr
from agent import Agent

css = """
body {
    background-image: url('https://media.licdn.com/dms/image/v2/D5612AQE56Y6FyBgOCQ/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1724087970185?e=2147483647&v=beta&t=awk5enaARMlrqSzHQy8KQTn6qR2fCnCh0b7ztrmrQrc'); /* Replace with your image URL or path */
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
}
"""

def main():
    with gr.Blocks() as JARVIS:
        
        Jarvis = gr.Chatbot()


    JARVIS.launch()


if __name__ == "__main__":
    main()