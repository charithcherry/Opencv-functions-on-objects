import cv2
import numpy as np


def atransform():
    img=cv2.imread('./venv/imgs/3.png')
    row,col,_=img.shape
    cv2.circle(img,(40,69),3,(0,0,255),-1)
    cv2.circle(img,(156,69),3,(0,0,255),-1)
    cv2.circle(img,(0,186),3,(0,0,255),-1)

    p1=np.float32([[40,69],[156,69],[40,186]])
    p2=np.float32([[40,69],[156,69],[80,186]])
    mat=cv2.getAffineTransform(p1,p2)
    result=cv2.warpAffine(img,mat,(row,col))
    cv2.imshow("Affine transformation",result)
    cv2.imshow("grid",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()