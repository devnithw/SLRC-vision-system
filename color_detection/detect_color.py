import cv2
import numpy as np

# Define the range of green and blue colors in HSV color space
green_lower = np.array([35, 50, 50])
green_upper = np.array([85, 255, 255])

blue_lower = np.array([110, 50, 50])
blue_upper = np.array([130, 255, 255])

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    if not ret:
        break

    # Convert to HSV format
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image to get only green colors
    mask_green = cv2.inRange(hsv, green_lower, green_upper)

    # Threshold the HSV image to get only blue colors
    mask_blue = cv2.inRange(hsv, blue_lower, blue_upper)

    # Count non-zero pixels in the masks
    green_pixels = cv2.countNonZero(mask_green)
    blue_pixels = cv2.countNonZero(mask_blue)

    # Output the detected color
    if green_pixels > blue_pixels:
        color_text = "Green"
    else:
        color_text = "Blue"

    # Display the shape on the frame
    cv2.putText(frame, color_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Display the frame
    cv2.imshow('Shape Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()