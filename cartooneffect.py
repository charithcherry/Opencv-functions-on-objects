import cv2
import numpy as np


def cartoon():

    cap=cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()

        #blurred=cv2.medianBlur(frame,5)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        gray=cv2.medianBlur(gray,9)
        edges=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,10)
        #edges=cv2.Canny(gray,75,150)

        color=cv2.bilateralFilter(frame,9,350,350)

        result=cv2.bitwise_and(color,color,mask=edges)

        #cv2.imshow("edges",edges)
        cv2.imshow("cartoon",result)
        cv2.imshow("frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()