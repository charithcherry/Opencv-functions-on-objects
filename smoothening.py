import cv2
import numpy as np


def smoothen():
    img=cv2.imread('./venv/imgs/4.jpg')
    avg=cv2.blur(img,(5,5))
    gauss=cv2.GaussianBlur(img,(15,15),0)
    med=cv2.medianBlur(img,5)
    bi=cv2.bilateralFilter(img,5,150,150)
    cv2.imshow("original",img)
    cv2.imshow("averaging",avg)
    cv2.imshow("Gaussian",gauss)
    cv2.imshow("median",med)
    cv2.imshow("bilateral",bi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()