# Machine Vision System for lLine Follower Robot (Sri Lanka Robotics Challenge 2024)
Computer Vision system for identifying 3D-objects and colors. Made for SLRC 2024. Powered by Tensorflow and OpenCV.

## Object Detection
One of the tasks of SLRC 2024 is for the robot to identify whether the object at the center of a ring is a cube or a cylinder. We tackled this task using computer vision. We experimented with the two approaches mentioned below. 

### Using Deep Learning
The robot includes a Raspberry Pi 4 Model B which runs a tensorflow model to inference. The video feed taken using a webcam is used for object classification. The deep learning model is trained using *MobileNetV1* as the base model with 2 dense layers attatched and trained using transfer learning. The training accuracy of this model reached 99%. 

The code for this technique can be found in `./object-detection` folder

### Using OpenCV edge detection
We also tried using OpenCV only to detect edges of the object in the center and generate contours. By hard-coding a specific number of contours as the threshold value, we can differentiate between the image of the cube and cylinder by comparing the number of contours generated. But we found this method is much more prone to errors. However the experimental code can be found in `./edge-detection`.

## Color Detection
Another task of SLRC 2024 is to identify the color of the wall infront of the line follower. Only two colors, green and blue, are possible. This could have been easily done with a color sensor module for Arduino. But since we have a camera fixed for the previous task, we implemented this functionality aslo from OpenCV. The code is much simpler and involves using two color masks for green and blue. Finally, the program counts the pixel area of green and blue seperately and outputs the color with the greater pixel area. The code for this task can be found in `./color-detection` folder.

## Final Driver Code
The final code running on the Raspberry Pi 4 Model B is included in the `main.py` file. This file consists of seperate functions `get_shape()` and `get_color()` which are called by the Raspberry Pi only when the Arduino Mega sends a request. The `main.py` file is run instantly after booting up the Raspberry Pi. 

## Technologies used
### Software
- Tensorflow and Keras
- OpenCV
- Google Colab to train the model
- Visual Studio Code

### Hardware
- Raspberry Pi 4 Model B
- Arduino Mega
- Hikvision Webcam
