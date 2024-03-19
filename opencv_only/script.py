import cv2
# Importing the Opencv Library
import numpy as np
# Importing NumPy,which is the fundamental package for scientific computing with #Python

# Reading Image
img = cv2.imread("")
cv2.namedWindow("Original Image",cv2.WINDOW_NORMAL)
# Creating a Named window to display image
cv2.imshow("Original Image",img)
# Display image

# RGB to Gray scale conversion
img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.namedWindow("Gray Converted Image",cv2.WINDOW_NORMAL)
# Creating a Named window to display image
cv2.imshow("Gray Converted Image",img_gray)
# Display Image

# Noise removal with iterative bilateral filter(removes noise while preserving edges)
noise_removal = cv2.bilateralFilter(img_gray,9,75,75)
cv2.namedWindow("Noise Removed Image",cv2.WINDOW_NORMAL)
# Creating a Named window to display image
cv2.imshow("Noise Removed Image",noise_removal)
# Display Image
# Thresholding the image
ret,thresh_image = cv2.threshold(noise_removal,0,255,cv2.THRESH_OTSU)
cv2.namedWindow("Image after Thresholding",cv2.WINDOW_NORMAL)
# Creating a Named window to display image
cv2.imshow("Image after Thresholding",thresh_image)
# Display Image

# Applying Canny Edge detection
canny_image = cv2.Canny(thresh_image,250,255)
cv2.namedWindow("Image after applying Canny",cv2.WINDOW_NORMAL)
# Creating a Named window to display image
cv2.imshow("Image after applying Canny",canny_image)
# Display Image
canny_image = cv2.convertScaleAbs(canny_image)

# dilation to strengthen the edges
kernel = np.ones((3,3), np.uint8)
# Creating the kernel for dilation
dilated_image = cv2.dilate(canny_image,kernel,iterations=1)
cv2.namedWindow("Dilation", cv2.WINDOW_NORMAL)
# Creating a Named window to display image
cv2.imshow("Dilation", dilated_image)
# Displaying Image
contours, h = cv2.findContours(dilated_image, 1, 2)
contours= sorted(contours, key = cv2.contourArea, reverse = True)[:1]
pt = (180, 3 * img.shape[0] // 4)
for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    # print len(cnt)
    print(len(approx))
    if len(approx) ==6 :
        print("Cube")
        cv2.drawContours(img,[cnt],-1,(255,0,0),3)
        cv2.putText(img,'Cube', pt ,cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, [0,255, 255], 2)
    elif len(approx) == 7:
        print("Cube")
        cv2.drawContours(img,[cnt],-1,(255,0,0),3)
        cv2.putText(img,'Cube', pt ,cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, [0, 255, 255], 2)
    elif len(approx) == 8:
        print("Cylinder")
        cv2.drawContours(img,[cnt],-1,(255,0,0),3)
        cv2.putText(img,'Cylinder', pt ,cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, [0, 255, 255], 2)
    elif len(approx) > 10:
        print("Sphere")
        cv2.drawContours(img,[cnt],-1,(255,0,0),3)
        cv2.putText(img,'Sphere', pt ,cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, [255, 0, 0], 2)

cv2.namedWindow("Shape", cv2.WINDOW_NORMAL)
cv2.imshow('Shape',img)

corners    = cv2.goodFeaturesToTrack(thresh_image,6,0.06,25)
corners    = np.float32(corners)
for    item in    corners:
    x,y    = item[0]
    cv2.circle(img,(x,y),10,255,-1)
cv2.namedWindow("Corners", cv2.WINDOW_NORMAL)
cv2.imshow("Corners",img)

cv2.waitKey()