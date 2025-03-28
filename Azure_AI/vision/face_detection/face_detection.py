from dotenv import load_dotenv
import os
import requests
import cv2
from PIL import Image
import numpy as np


class FaceDetectionClient():

    def __init__(self):

        load_dotenv()

        self.API_VISION_ENDPONT = ""
        self.API_VISION_KEY = ""

        self.CASCADE_PATH = os.getenv("CASCADE_PATH")
        self.CASCADE = cv2.CascadeClassifier(self.CASCADE_PATH)

    
    def face_detection(self, image):
        # TODO:
        """
        1. Convert image's RGB metadata into BGR format
        2. Convert original image into numpy data type
        """
        image = cv2.cvtColor(image, cv2.Color_RGB2BGR)

        faces = self.CASCADE.detectMultiScale(
            image = image,
            scaleFactor = 1.1,
            minNeighbors = 5,
            minSize = (30, 30)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img = image, pt1 = (x, y), pt2 = (x + w, y + h), color = (0, 255, 0), thickness = 2)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        return image
    

if __name__ == "__main__":
    client = FaceDetectionClient()