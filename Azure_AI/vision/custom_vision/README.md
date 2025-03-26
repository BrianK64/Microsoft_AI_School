# Microsoft Azure AI Services - Custom Vision Documentation

## Table of Contnets
- Prerequisites
- Set-Up


## Prerequisites
- Azure Subscription

- Azure Resource Group

- Azure AI Custom Vision Resource

- Python Version 3.x

    - Require pip for package installations


## Set-Up

1. Installing the client library
    
    Run the following command in PowerShell or a console window

    `pip install azure-cognitiveservices-vision-customvision`

2. Importing required libraries

    Create a new Python file and import the following libraries.

    ```python
    from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
    from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
    from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
    from msrest.authentication import ApiKeyCredentials
    import os, time, uuid
    ```

3. Create environment variables

    These authentical credentials are required to utilize full functionalities of Custom Vision

    - `VISION_TRAINING_KEY`
    - `VISION_TRAINING_ENDPOINT`
    - `VISION_PREDICTION_KEY`
    - `VISION_PREDICTION_ENDPOINT`
    - `VISION_PREDICTION_RESOURCE_ID`