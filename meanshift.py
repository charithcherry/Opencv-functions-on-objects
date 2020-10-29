import  cv2
import  numpy as np



def meanshift_liv():
    cap=cv2.VideoCapture(0)
    roi=cv2.imread("./venv/imgs/22.png")
    hsv_roi=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    roi_hist=cv2.calcHist([hsv_roi],[0],None,[180],[0,180])
    roi_hist=cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
    term=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,1 )


    while True:
        _,frame=cap.read()

        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        mask=cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        _,track_window=cv2.meanShift(mask,(300,305,roi.shape[1],roi.shape[0]),term)
        x,y,w,h =track_window
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow("mask",mask)


        cv2.imshow("frame",frame)
        key=cv2.waitKey(60)
        if key==27:
            break
    cap.release()
    cv2.destroyAllWindows()