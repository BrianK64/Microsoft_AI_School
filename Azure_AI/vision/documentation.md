# Microsoft Azure AI Services - Computer Vision Documentation
Disclaimer: This documentation is an user-friendly quickstart for personal development, experiments, and deployment. Please refer to the official Microsoft Azure Documentation for more concise and technical support.

## Table of Contents
- Prerequisites
- Azure Portal
- Vision Studio
- Authentication Credentials
- Query Parameters
- Request Body Format
- API Call


## Prerequisites
- Azure Subscription

- Azure Resource Group

- Azure AI Computer Vision Resource

    - Each feature has varying region accessibility requirements.

    - Please refer to the Azure Portal section for details.


## Azure Portal

This section demonstrates required resource(s) as well as directions for further steps.

1. Navigate to the Microsoft Azure portal.

2. Sign in to the Microsoft Azure portal using credentials associated with an active Azure subscription.

3. Create a resource group in which an Azure AI Computer Vision resource will be initiated.

4. Create an Azure AI Computer Vision resource within the resoure group.

    - Regional availability for Image Analysis tasks within the Azure AI Computer Vision Service are as followings:

    | Region | Image Analysis | Image Captioning | Product Regognition | Multimodal Embeddings | Background Removal |
    |--------|:--------------:|:----------------:|:-------------------:|:---------------------:|:------------------:|
    | East US | ✅ | ✅ | ✅ | ✅ | ✅ |
    | West US | ✅ | ✅ | | ✅ | ✅ |
    | West US 2| ✅ | | ✅ | ✅ | |
    | France Central | ✅ | ✅ | | ✅ | ✅ |
    | North Europe | ✅ | ✅ | | ✅ | ✅ |
    | West Europe | ✅ | ✅ | | ✅ | ✅ |
    | Sweden Central | ✅ |  | | ✅ | |
    | Switzerland North | ✅ | | | ✅ | |
    | Australia East | ✅ | | | ✅ | |
    | Southeast Asia | ✅ | ✅ | | ✅ | ✅ |
    | East Asia | ✅ | ✅ | | | |
    | Korea Central | ✅| ✅ | | ✅ | ✅ |
    | Japan East | ✅ | | | ✅ | |



## Vision Studio

### Image Analysis Features

    Description for each Azure AI Computer Vision Image Analysis feature

| FEATURE | DESCRIPTION |
|---------|-------------|
| Image Retrieval | Retrieve specific moments within an image set |
| Dense Captioning | Generate human-readable captions for all important objects detecteddd in an image. |
| Captioning | Generate a human-readable sentnece that described the content of an image. |
| Object Detection | Recognize the location of objects of interest in an image and assing them a label. |
| Tag Extraction | Use an AI model to automatically assign one or more labels to an image. |
| Image Cropping | Create cropped image thumbnails based on the key areas of a larger image. |


## Authentication Credentials

### Credentials

To access and utilize the Image Analysis service within Azure AI Services, user must first authenticate by providing two specific credential information:

1. `ENDPOINT`: This endpoint URL is the specific web address of the Azure service to which API requests will be sent.

2. `KEY`: A secret API key, acting as an authentication token, to ensure secure interactions between authorized user(s) and corresponding service.

This credential information is automoatically generated and assigned upon Azure resource creation.

### Locating Credentials

Here's a brief step-by-step walkthorugh for locating the credential information in the Azure portal:

1. Navigate to the Azure Portal and sign in.

2. Access the Computer Vision resource.

3. Go to the Resource Management tab.
    
    - On the resource's overview page, click on the Resource Management section.

4. Locate the kEYs and ENDPOINT.

    - `KEY 1`: Primary authentication key.
    - `KEY 2`: Secondary (spare) authentication key.
    - `Endpoint`: The service endpoint URL for created region.