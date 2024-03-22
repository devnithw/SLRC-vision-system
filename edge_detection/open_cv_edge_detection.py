import cv2
import numpy as np

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

while True:
    ret, img= cap.read()
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.namedWindow("Grey", cv2.WINDOW_NORMAL)
    cv2.imshow('Grey',img_gray)
    # noise_removal = cv2.bilateralFilter(img_gray,9,75,75)
    ret,thresh_image = cv2.threshold(img_gray,75 ,255,cv2.THRESH_BINARY)
    cv2.namedWindow("Threshold", cv2.WINDOW_NORMAL)
    cv2.imshow('Threshold',thresh_image) 
    canny_image = cv2.Canny(thresh_image,250,255)
    canny_image = cv2.convertScaleAbs(canny_image)
    kernel = np.ones((3,3), np.uint8)
    dilated_image = cv2.dilate(canny_image,kernel,iterations=1)

    cv2.namedWindow("Dilated", cv2.WINDOW_NORMAL)
    cv2.imshow('Dilated',dilated_image)

    contours, h = cv2.findContours(dilated_image, 1, 2)
    contours= sorted(contours, key = cv2.contourArea, reverse = True)[:1]
    pt = (180, 3 * img.shape[0] // 4)
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
        # print len(cnt)
        print(len(approx))
        if len(approx) <= 8 :
            print("Cube")
            cv2.drawContours(img,[cnt],-1,(255,0,0),3)
            cv2.putText(img,'Cube', pt ,cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, [0,255, 255], 2)
        else:
            print("Cylinder")
            cv2.drawContours(img,[cnt],-1,(255,0,0),3)
            cv2.putText(img,'Cylinder', pt ,cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, [255, 0, 0], 2)

    cv2.namedWindow("Final", cv2.WINDOW_NORMAL)
    cv2.imshow('Final',img)
    

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()