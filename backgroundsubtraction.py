import cv2
import numpy as np


def sub():
    cap=cv2.VideoCapture("./venv/imgs/highway.mp4")
    _,ff=cap.read()
    ffg=cv2.cvtColor(ff,cv2.COLOR_BGR2GRAY)
    ffg=cv2.GaussianBlur(ffg,(5,5),0)
    while True:
        _, frame=cap.read()
        gf = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gf=cv2.GaussianBlur(gf,(5,5),0)
        diff=cv2.absdiff(ffg,gf)
        _,diff=cv2.threshold(diff,25,255,cv2.THRESH_BINARY)


        cv2.imshow("diff",diff)
        cv2.imshow("frame",frame)
        key=cv2.waitKey(30)
        if key ==27:
            break
    cap.release()
    cv2.destroyAllWindows()


def subtractor():
    cap = cv2.VideoCapture("./venv/imgs/highway.mp4")
    subtract=cv2.createBackgroundSubtractorMOG2(history=20,varThreshold=25,detectShadows=False)
    while True:
        _, frame = cap.read()

        mask=subtract.apply(frame)
        cv2.imshow("frame", frame)
        cv2.imshow("mask",mask)
        key = cv2.waitKey(30)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()