import numpy as np
from tensorflow.keras.models import load_model

def predict_image(model, preprocessed_image):
    prediction = model.predict(preprocessed_image)
    return prediction

def describe_prediction(prediction):
    if np.max(prediction) > 0.5:
        return "The model predicts that the image contains cancerous regions."
    else:
        return "The model predicts that the image does not contain cancerous regions."
