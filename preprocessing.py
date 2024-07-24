import numpy as np
import cv2

def preprocess_image(image_path, shape=256):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (shape, shape))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img
