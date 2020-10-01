import cv2
import numpy as np


def cordet():
    img=cv2.imread('./venv/imgs/10.jpg')
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    corner=cv2.goodFeaturesToTrack(gray,100,0.01,10)
    corner=np.int0(corner)
    for c in corner:
        x,y=c.ravel()
        cv2.circle(img,(x,y),3,(0,255,0),-1)
    cv2.imshow("img",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def nothing():
    pass

def cordetliv():
    cap=cv2.VideoCapture(0)
    cv2.namedWindow("frame")
    cv2.createTrackbar("quality","frame",1,100,nothing)
    while True:
        _,frame=cap.read()
        value=cv2.getTrackbarPos("quality","frame")
        value=value/100 if value>0 else 0.01
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corner = cv2.goodFeaturesToTrack(gray, 100, value, 20)
        if corner is not None:
            corner = np.int0(corner)
            for c in corner:
              x, y = c.ravel()
              cv2.circle(frame, (x, y), 3, (0, 0,255), -1)
        cv2.imshow("frame",frame)
        key=cv2.waitKey(1)
        if key==27:
            break
    cap.release()
    cv2.destroyAllWindows()