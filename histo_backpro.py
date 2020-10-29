import cv2
import numpy as np
from matplotlib import pyplot as plt

def histogram_back_projection():
    oimg=cv2.imread("./venv/imgs/20.jpg")
    roi=cv2.imread("./venv/imgs/21.jpg")
    ohsv=cv2.cvtColor(oimg,cv2.COLOR_BGR2HSV)
    roi_hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    roi_hist=cv2.calcHist([roi_hsv],[0,1],None,[180,256],[0,180,0,256])
    hue, saturation , value= cv2.split(roi_hsv)

    mask=cv2.calcBackProject([ohsv],[0,1],roi_hist,[0,180,0,256],1)
    kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    mask =cv2.filter2D(mask,-1,kernel)
    _,mask=cv2.threshold(mask,100,255,cv2.THRESH_BINARY)

    mask=cv2.merge((mask,mask,mask))
    result=cv2.bitwise_and(oimg,mask)
    cv2.imshow("mask",mask)
    cv2.imshow("original",ohsv)
    cv2.imshow("result",result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()