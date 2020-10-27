import cv2
import numpy as np

draw=False
p1 = ()
p2 = ()

def mou():
    def mouse_drawing(event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            print("left click")
            circles.append((x,y))


    cap=cv2.VideoCapture(0)
    cv2.namedWindow("video")
    cv2.setMouseCallback("video",mouse_drawing)
    circles=[]
    while True:
        _,frame=cap.read()
        for c in circles:
            cv2.circle(frame,c,5,(0,0,255),-1)


        cv2.imshow("video",frame)
        key=cv2.waitKey(1)
        if key==27:
            break
        elif key==ord('d'):
            circles=[]
    cap.release()
    cv2.destroyAllWindows()


def rect():
    def mouse_drawing(event, x, y, flags, params):
        global p1,p2,draw
        if event == cv2.EVENT_LBUTTONDOWN:
           if draw is False:
            draw=True
            p1=(x,y)
           else:
               draw=False

        elif event==cv2.EVENT_MOUSEMOVE:
            if draw is True:
                p2=(x,y)




    cap=cv2.VideoCapture(0)
    cv2.namedWindow("video")
    cv2.setMouseCallback("video",mouse_drawing)
    while True:
        _,frame=cap.read()
        if p2 and p1:
            cv2.rectangle(frame,p1,p2,(0,255,0))


        cv2.imshow("video",frame)
        key=cv2.waitKey(1)
        if key==27:
            break

    cap.release()
    cv2.destroyAllWindows()