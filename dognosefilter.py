import cv2
import numpy as np
import dlib
from math import hypot


def dognose():
    cap=cv2.VideoCapture(0)
    detector=dlib.get_frontal_face_detector()
    predictor=dlib.shape_predictor("./venv/imgs/shape_predictor_68_face_landmarks.dat")
    nose=cv2.imread("./venv/imgs/28.png")
    _,frame=cap.read()
    rows, cols, _ = frame.shape
    nose_mask = np.zeros((rows, cols), np.uint8)
    while True:
        _,frame=cap.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


        faces=detector(frame)
        for face in faces:
            landmarks=predictor(gray,face)

            center_nose=(landmarks.part(30).x,landmarks.part(30).y)
            top_nose=(landmarks.part(29).x,landmarks.part(29).y)
            left_nose = (landmarks.part(31).x, landmarks.part(31).y)
            right_nose=(landmarks.part(35).x,landmarks.part(35).y)



            nose_width=int(hypot(left_nose[0]-right_nose[0],left_nose[1]-right_nose[1])*1.7)
            nose_height=int(nose_width*0.78)
            nose_dog=cv2.resize(nose,(nose_width,nose_height))
            nose_dog_gray = cv2.cvtColor(nose_dog, cv2.COLOR_BGR2GRAY)
            _,nose_mask=cv2.threshold(nose_dog_gray,100,255,cv2.THRESH_BINARY)


            top_left=(int(center_nose[0]-nose_width/2),int(center_nose[1]-nose_height/2))
            bottom_right=(int(center_nose[0]+nose_width/2),int(center_nose[1]+nose_height/2))

           # cv2.rectangle(frame,(int(center_nose[0]-nose_width/2),int(center_nose[1]-nose_height/2)),
            #              (int(center_nose[0]+nose_width/2),int(center_nose[1]+nose_height/2)),(0,255,0),2)

            nose_area=frame[top_left[1]:top_left[1]+nose_height,top_left[0]:top_left[0]+nose_width]
            nose_area_no_nose=cv2.bitwise_and(nose_area,nose_area,mask=nose_mask)
            final_nose=cv2.add(nose_area_no_nose,nose_dog)
            #frame[top_left[1]:top_left[1]+nose_height,top_left[0]:top_left[0]+nose_width]=final_nose

            #cv2.imshow("nose area",nose_area)
            #cv2.imshow("nose dog",nose_dog)
            #cv2.imshow("mask",nose_mask)
            cv2.imshow("final",final_nose)
            #cv2.imshow("no",nose_area_no_nose)
        cv2.imshow("frame",frame)
        key=cv2.waitKey(1)
        if key==27:
            break
    cap.release()
    cv2.destroyAllWindows()

