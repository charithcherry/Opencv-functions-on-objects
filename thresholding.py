import numpy as np
import cv2



def nothing():
    pass





def thresh ():
  cv2.namedWindow('image')
  cv2.createTrackbar("Threshold value", "image", 12, 255, nothing)
  while True:
    value=cv2.getTrackbarPos("Threshold value","image")
    img=cv2.imread('./venv/imgs/2.jpg',cv2.IMREAD_GRAYSCALE)
    _,threshold_binary=cv2.threshold(img,value,255,cv2.THRESH_BINARY)
    _,threshold_binary_inv=cv2.threshold(img,value,255,cv2.THRESH_BINARY_INV)
    _,threshold_trunc=cv2.threshold(img,value,255,cv2.THRESH_TRUNC)
    _,threshold_o=cv2.threshold(img,value,255,cv2.THRESH_TOZERO)
    _,threshold_o_inv=cv2.threshold(img,value,255,cv2.THRESH_TOZERO_INV)
    cv2.imshow("image",img)
    cv2.imshow("binary",threshold_binary)
    cv2.imshow("binary_inv",threshold_binary_inv)
    cv2.imshow("thresh_runc",threshold_trunc)
    cv2.imshow("to zero",threshold_o)
    cv2.imshow("zero inverse",threshold_o_inv)
    key = cv2.waitKey(1)
    if key == 27:
        break

  cv2.waitKey(0)
  cv2.destroyAllWindows()

