import cv2
import numpy as np

# Define the range of green and blue colors in HSV color space
green_lower = np.array([35, 50, 50])
green_upper = np.array([85, 255, 255])

blue_lower = np.array([110, 50, 50])
blue_upper = np.array([130, 255, 255])

# Set camera (Set 0 when testing in Pi, set 1 when testing using webcam in PC)
cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

def get_color():
    # Read a frame from the camera
    ret, frame = cap.read()

    if not ret:
        return -1
    
    # Convert to HSV format
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image to get only green or blue colors
    mask_green = cv2.inRange(hsv, green_lower, green_upper)
    mask_blue = cv2.inRange(hsv, blue_lower, blue_upper)

    # Count non-zero pixels in the masks
    green_pixels = cv2.countNonZero(mask_green)
    blue_pixels = cv2.countNonZero(mask_blue)

    # Output the detected color (0 - green, 1 - blue)
    if green_pixels > blue_pixels:
        color_text = 0
    else:
        color_text = 1
    
    return color_text
    