import cv2
import  numpy as np
# can be used as a face filter
#top bulged filter
#define points[p1] based on object in front
def transform():
    cap=cv2.VideoCapture(0)
    while True:
        _,frame=cap.read()
        p1=np.float32([[155,120],[480,120],[20,475],[620,475]])
        p2=np.float32([[10,0],[400,0],[0,600],[400,600]])
        mat=cv2.getPerspectiveTransform(p1,p2)
        res=cv2.warpPerspective(frame,mat,(400,600))
        cv2.imshow("frame",frame)
        cv2.imshow("perspective",res)
        key=cv2.waitKey(1)
        if key==27:
            break



    cap.release()
    cv2.destroyAllWindows()