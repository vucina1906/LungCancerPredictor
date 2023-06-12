import sys
from exception import CustomException
import os
from tensorflow.keras.models import load_model
import cv2
import numpy as np
from tensorflow.keras.applications.efficientnet import preprocess_input

INPUT_SHAPE = (250, 250, 3)
CATEGORIES = ["adenocarcinoma", "largecellcarcinoma", "squamouscellcarcinoma", "normal"]

def load_object(file_path, model_file):
    try:
        model_path = os.path.join(file_path, model_file)
        model = load_model(model_path)
        return model
    except Exception as e:
        raise CustomException(e, sys)
    

def preprocess(filepath):
    img = cv2.imread(filepath)
    img = cv2.resize(img, (INPUT_SHAPE[1], INPUT_SHAPE[0]))
    img = np.reshape(img, (1,) + INPUT_SHAPE)
    img = preprocess_input(img) 
    return img

def predict_single_image(filepath, imported_model):
    img = preprocess(filepath)
    prediction = imported_model.predict(img)
    predicted_class_index = np.argmax(prediction[0])
    predicted_class = CATEGORIES[predicted_class_index]
    return predicted_class


