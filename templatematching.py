import cv2
import numpy as np


def temp():
    img=cv2.imread('./venv/imgs/7.png')
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    t=cv2.imread('./venv/imgs/8.jpg',cv2.IMREAD_GRAYSCALE)
    temp=cv2.resize(t,(400,300),0,0)
    w,h,=temp.shape[::-1]
    res=cv2.matchTemplate(grayimg,temp,cv2.TM_CCORR_NORMED)
    loc=np.where(res>=0.5)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,255,0),3)
    cv2.imshow("img",img)
    cv2.imshow("template",temp)
    cv2.imshow("result",res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def templive():
    cap=cv2.VideoCapture(0)
    t=cv2.imread("./venv/imgs/9.JPG",cv2.IMREAD_GRAYSCALE)
    temp=cv2.resize(t,(300,350),0,0)
    w,h=temp.shape[::-1]
    while True:
        _,frame=cap.read()
        gframe=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        res=cv2.matchTemplate(gframe,temp,cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.55)
        for pt in zip(*loc[::-1]):
           cv2.rectangle(frame,pt,(pt[0]+w,pt[1]+h),(0,255,0),3)
        cv2.imshow("frame",frame)
        cv2.imshow("pic",temp)
        key=cv2.waitKey(1)
        if key==27:
            break
    cap.release()
    cv2.destroyAllWindows()