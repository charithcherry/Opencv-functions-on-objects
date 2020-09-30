import  cv2
import numpy as np

def linedet():
    img=cv2.imread('./venv/imgs/10.jpg')
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges=cv2.Canny(gray,75,150)
    lines=cv2.HoughLinesP(edges,1,np.pi/180,10,maxLineGap=250)
    for line in lines:
        x1,y1,x2,y2=line[0]
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),3)
    cv2.imshow("edges",edges)
    cv2.imshow("image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def linevdet():
    video=cv2.VideoCapture(0)
    while True:
        ret,oframe=video.read()
        frame=cv2.GaussianBlur(oframe,(5,5),0)
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        ly=np.array([18,94,140])
        uy=np.array([48,255,255])
        mask=cv2.inRange(hsv,ly,uy)
        edges=cv2.Canny(mask,75,150)
        lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, maxLineGap=250)
        if lines is not None:
         for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
        cv2.imshow("edges",edges)
        cv2.imshow("frame",frame)
        key=cv2.waitKey(1)
        if key==27:
            break
    video.release()
    cv2.destroyAllWindows()