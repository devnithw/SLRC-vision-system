import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# Constants
IMAGE_SIZE = 224

def preprocess_img(img):
    # Resize image to match model input size
    img = cv2.resize(img, (IMAGE_SIZE, IMAGE_SIZE))

    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)

    # Get MobileNet preprocess
    img = preprocess_input(img)
    return img

# Load the trained model
model = load_model('model_final.h5')

# Function to perform shape detection
def detect_shape(frame):
    # Preprocess the frame
    img = preprocess_img(frame)

    # Predict the shape
    predictions = model.predict(img)
    print(predictions)
    shape_index = np.argmax(predictions)

    # Define shape labels
    shape_labels = {0: 'cube', 1: 'cylinder'}

    return shape_labels[shape_index]

def get_shape():
    # Open camera
    capture = cv2.VideoCapture(0)
    capture.set(3, 640)
    capture.set(4, 480)

    # Read a frame from the camera
    ret, frame = capture.read()

    # Return -1 if error
    if not ret:
        return -1
    
    # Perform shape detection on the frame
    shape = detect_shape(frame)

    # Returns "cube" if cube and "cylinder" if Cylinder
    return shape
