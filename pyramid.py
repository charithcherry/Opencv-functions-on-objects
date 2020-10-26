import cv2
import numpy as np

def pyr():
    img= cv2.imread("./venv/imgs/1.jpg")
    layer=img.copy()
    gp=[layer]
    for i in range(6):
        layer=cv2.pyrDown(layer)
        gp.append(layer)
    layer=gp[5]
    lappy=[layer]
    for i in range(5,0,-1):
        size=(gp[i-1].shape[1],gp[i-1].shape[0])
        ge=cv2.pyrUp(gp[i],dstsize=size)
        lap=cv2.subtract(gp[i-1],ge)
        lappy.append(lap)
    rec=lappy[0]
    for i in range(1,6):
        size=(lappy[i].shape[1],lappy[i].shape[0])
        rec=cv2.pyrUp(rec,dstsize=size)
        rec=cv2.add(rec,lappy[i])
        cv2.imshow(str(i),rec)


    cv2.imshow("original",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


