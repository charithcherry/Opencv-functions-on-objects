import cv2
import numpy as np


def det():
    img=cv2.imread('./venv/imgs/5.jpg',cv2.IMREAD_GRAYSCALE)
    simg=cv2.resize(img,(300,300),0,0)
    gimg=cv2.GaussianBlur(simg,(5,5),0)

    sobx=cv2.Sobel(gimg,cv2.CV_64F,1,0)
    soby=cv2.Sobel(gimg,cv2.CV_64F,0,1)

    lap=cv2.Laplacian(gimg,cv2.CV_64F,ksize=5)
    canny=cv2.Canny(gimg,100,150)


    cv2.imshow("original",simg)
    cv2.imshow("x",sobx)
    cv2.imshow("y",soby)
    cv2.imshow("laplacian",lap)
    cv2.imshow("canny",canny)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def livdet():
    cap=cv2.VideoCapture(0)
    while True:
        _,frame=cap.read()
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        blur=cv2.GaussianBlur(frame,(5,5),0)
        lap=cv2.Laplacian(blur,cv2.CV_64F)
        canny=cv2.Canny(blur,100,150)


        cv2.imshow("frame",frame)
        cv2.imshow("laplacian",lap)
        cv2.imshow("canny",canny)
        key=cv2.waitKey(1)
        if key==27:
            break
    cap.release()
    cv2.destroyAllWindows()