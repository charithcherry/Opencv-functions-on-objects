import  cv2
import numpy as np


def cam():
    img=cv2.imread("./venv/imgs/24.jpg")
    img=cv2.resize(img,(300,400))
    roi=img[0:250,0:250]
    x=0
    y=0
    width=250
    height=250
    cap=cv2.VideoCapture(0)
    hsv_roi=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    roi_hist=cv2.calcHist([hsv_roi],[0],None,[180],[0,180])
    term=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,1)

    while True:
        _,frame=cap.read()
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        mask=cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        ret ,track=cv2.CamShift(mask,(x,y,width,height),term)

        pts=cv2.boxPoints(ret)
        pts=np.int0(pts)

        cv2.polylines(frame,[pts],True,(255,0,0),2)
        cv2.imshow("mask",mask)
        cv2.imshow("frame",frame)
        key=cv2.waitKey(1)
        if key==27:
            break




    cap.release()
    cv2.destroyAllWindows()