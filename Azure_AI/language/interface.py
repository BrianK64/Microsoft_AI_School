import gradio as gr
from agent import Agent


def main():
    agent = Agent()

    with gr.Blocks() as demo:

        # A set of available features in Azure AI Language Service
        features = [
            "NER",                      # Named Entity Recognition
            "PII",                      # Personally Identifiable Information Detection
            "Key Phrase",               # Key Phrase Extraction
            "Sentiment",                # Sentiment Analysis
            "Language Detection",       # Language Detection
            "CLU"                       # Conversational Language Understanding
        ]

        feature_descriptions = {
            "NER": "Named Entity Recognition identifies entities like people, organizations, and locations in the text.",
            "PII": "Personally Identifiable Information detection finds personal information like names, addresses, or social security numbers.",
            "Key Phrase": "Key Phrase Extraction identifies important words or phrases that summarize the text.",
            "Sentiment": "Sentiment Analysis determines the overall sentiment (positive, neutral, negative) of the text.",
            "Language Detection": "Language Detection identifies the language of the text.",
            "CLU": "Conversational Language Understanding helps in extracting meaning from natural language conversations."
        }

        def get_radio(feature):
            return feature
        
        def get_description(feature):
            return feature_descriptions.get(feature, "Select a service to see its description.")
        
        def process(feature, text):
            log = {
                "feature": feature,
                "text": text
            }
            print(log)

            if feature == "NER":
                response = agent.named_entity_recognition(text = text)

            elif feature == "PII":
                response = agent.PII_detection(text = text)

            elif feature == "Key Phrase":
                response = agent.key_phrase_extraction(text = text)

            elif feature == "Sentiment":
                response = agent.sentiment_analysis(text = text)

            elif feature == "Language Detection":
                response = agent.language_detection(text = text)

            elif feature == "CLU":
                response = agent.clu(text = text)
            
            else:
                return None
            
            return response

        # Azure AI I/O components
        feature_radio = gr.Radio(label = "Available Azure AI Language Services", choices = features)
        feature_description = gr.Text(label = "Service Description", placeholder = "Select a service to see its description.", lines = 2, interactive = False)
        input_textbox = gr.Textbox(label = "Input", lines = 10)
        process_button = gr.Button("Process")
        output_textbox = gr.Textbox(label = "Output", lines = 10)

        feature_radio.change(get_description, inputs = [feature_radio], outputs = [feature_description])
        #feature_description.change(get_description, inputs = [feature_radio], outputs = [feature_description])
        process_button.click(process, inputs = [feature_radio, input_textbox], outputs = [output_textbox])

    demo.launch()


if __name__ == "__main__":
    main()