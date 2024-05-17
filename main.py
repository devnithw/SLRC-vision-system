import cv2
import numpy as np
import time
import RPi.GPIO as GPIO
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define GPIO pins
led_cube = 17
led_cyl = 27
color_input = 22
shape_input = 4
GPIO.setup(led_cube, GPIO.OUT)
GPIO.setup(led_cyl, GPIO.OUT)
GPIO.setup(color_input, GPIO.IN)
GPIO.setup(shape_input, GPIO.IN)
GPIO.output(led_cube, GPIO.LOW)
GPIO.output(led_cyl, GPIO.LOW)

# Define the range of green and blue colors in HSV color space
green_lower = np.array([35, 50, 50])
green_upper = np.array([85, 255, 255])

blue_lower = np.array([110, 50, 50])
blue_upper = np.array([130, 255, 255])

def get_color(frame):
    """
    Returns a color of a input camera frame by selectively masking green and blue colors. Runs using OpenCV only.
    input - VideoCapture frame
    output - text saying 'green' or 'blue'
    """
    # Convert to HSV format
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image to get only green or blue colors
    mask_green = cv2.inRange(hsv, green_lower, green_upper)
    mask_blue = cv2.inRange(hsv, blue_lower, blue_upper)

    # Count non-zero pixels in the masks
    green_pixels = cv2.countNonZero(mask_green)
    blue_pixels = cv2.countNonZero(mask_blue)

    # Output the detected color (green, blue)
    if green_pixels > blue_pixels:
        color_text = 'green'
    else:
        color_text = 'blue'
    return color_text

def preprocess_img(img):
    """
    Preprocess an image frame to be sent through the MobileNetV1 Model and outputs it as a numpy array. 
    input - Video capture frame
    output - Preprocessed image as numpy arrau
    """
    img = cv2.resize(img, (224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    return img

# Load the trained model (MobilenetV1)
model = load_model('/home/januka_pi/Documents/GitHub/SLRC-vision/model_final.h5')

def detect_shape(frame):
    """
    Returns the shape detected in a image frame using a custom trained MobileNetV1 model trained using Tensorflow backend.
    Binary classifies the image considering whether the present object is a cube or a cylinder.
    input - image frame
    output - text saying 'cube' or 'cylinder'
    """
    # Preprocess the frame
    img = preprocess_img(frame)

    # Predict the shape
    predictions = model.predict(img)
    shape_index = np.argmax(predictions)
    print(predictions)

    # Define shape labels
    shape_labels = {0: 'cube', 1: 'cylinder'}

    return shape_labels[shape_index]

# Start webcam connection
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# By this point every setup is successful
print("Everything ready")

# Main loop
try:
    while True:
        # Read data from Arduino (If checking color, color_state is high. If checking shape, shape_state is high)
        color_state = GPIO.input(color_input)
        shape_state = GPIO.input(shape_input)

        # Detect color
        if color_state == 1: 
            # Read a frame from the camera
            ret, frame = cap.read()

            # Perform color detection on the frame
            color = get_color(frame)

            if color == "green":
                GPIO.output(led_cube, GPIO.HIGH)
                GPIO.output(led_cyl, GPIO.LOW)
            else:
                GPIO.output(led_cyl, GPIO.HIGH)
                GPIO.output(led_cube, GPIO.LOW)
        
        # Detect shape
        if shape_state == 1: 
            # Read a frame from the camera
            ret, frame = cap.read()

            # Perform shape detection on the frame
            shape = detect_shape(frame)

            if shape == "cube":
                GPIO.output(led_cube, GPIO.HIGH)
                GPIO.output(led_cyl, GPIO.LOW)
            else:
                GPIO.output(led_cyl, GPIO.HIGH)
                GPIO.output(led_cube, GPIO.LOW)             
except KeyboardInterrupt:
    print("Exiting...")
    cap.release()
