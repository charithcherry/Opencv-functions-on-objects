import cv2
import numpy as np

def nothing():
    pass
def livcon():
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('tracker')
    cv2.createTrackbar("L-H", "tracker", 0, 179, nothing)  # L - lower U-upper limits
    cv2.createTrackbar("L-S", "tracker", 0, 255, nothing)
    cv2.createTrackbar("L-V", "tracker", 0, 255, nothing)
    cv2.createTrackbar("U-H", "tracker", 179, 179, nothing)
    cv2.createTrackbar("U-S", "tracker", 255, 255, nothing)
    cv2.createTrackbar("U-V", "tracker", 255, 255, nothing)
    while True:
        _, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lh = cv2.getTrackbarPos('L-H', 'tracker')
        ls = cv2.getTrackbarPos('L-S', 'tracker')
        lv = cv2.getTrackbarPos('L-V', 'tracker')
        uh = cv2.getTrackbarPos('U-H', 'tracker')
        us = cv2.getTrackbarPos('U-S', 'tracker')
        uv = cv2.getTrackbarPos('U-V', 'tracker')
        lower_blue = np.array([lh, ls, lv])
        upper_blue = np.array([uh, us, uv])

        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        c, _ =cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        for co in c:
            area=cv2.contourArea(co)
            if area>1000:
                cv2.drawContours(frame,co,-1,(0,255,0),3)
        cv2.imshow("frame",frame)
        cv2.imshow("mask",mask)
        key=cv2.waitKey(1)
        if key==27:
            break
    cap.release()
    cv2.destroyAllWindows()