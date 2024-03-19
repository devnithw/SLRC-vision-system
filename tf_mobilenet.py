import cv2
import numpy as np
from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# the parameters
IMAGE_SIZE = 224
ALPHA=0.75
EPOCHS=20

def preprocess_img(img):
    img = cv2.resize(img, (224, 224))  # Resize image to match model input size
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
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
    shape_labels = {0: 'Cube', 1: 'Cylinder'}

    return shape_labels[shape_index]

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    if not ret:
        break

    # Perform shape detection on the frame
    shape = detect_shape(frame)

    # Display the shape on the frame
    cv2.putText(frame, shape, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Display the frame
    cv2.imshow('Shape Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()