# Microsoft Azure Speech
## Setup
### Prerequisites
* Microsoft Azure subscription.
* Azure AI Services Speech Service resource.
### Speech CLI environment
* dotnet
## Speech to Text
### Speech Recognition
* Speech Recognition with Microphone Input:\
`spx recognize --microphone`
### Speech Translation
* Tranlsating an input audio stream into a target language:\
`spx translate --microphone --source <INPUT_LANGUAGE> --target <OUTPUT_LANGUAGE>`
## Text to Speech
### Speech Synthesis
* Synthesize speech from text:\
`spx synthesize --text <YOUR_TEXT_GOES_HERE>`
## Resources
https://learn.microsoft.com/en-us/azure/ai-services/speech-service/