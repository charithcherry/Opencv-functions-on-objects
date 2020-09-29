import cv2
import numpy as np


def adap():
    img=cv2.imread('./venv/imgs/2.jpg')
    _,thresh=cv2.threshold(img,150,255,cv2.THRESH_BINARY)
    imgg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    meanc=cv2.adaptiveThreshold(imgg,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,10)
    gauss=cv2.adaptiveThreshold(imgg,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,10)


    cv2.imshow('original',img)
    cv2.imshow('thresh',thresh)
    cv2.imshow('mean c',meanc)
    cv2.imshow('gaussian',gauss)
    cv2.waitKey(0)
    cv2.destroyAllWindows()