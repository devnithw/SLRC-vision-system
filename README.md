# 3d-shape-detection
Computer Vision system for identifying cubes and cylinders using Deep Learning. Made for SLRC 2024.

## Object Detection

### Using Deep Learning
One of the tasks of SLRC 2024 is for the robot to identify whether the object at the center of a ring is a cube or a cylinder. We tackled this task through computer vision. The robot includes a Raspberry Pi 4 Model B which runs a tensorflow model to inference. The video feed taken using a webcam is used for object classification. The deep learning model is trained using MobileNet as the base model with 2 dense layers attatched and trained using transfer learning. The training accuracy of this model reached 98%. 

The code for this technique can be found in the main python file tf_mobilenet.py

### Using OpenCV edge detection
TODO

## Color Detection
TODO
