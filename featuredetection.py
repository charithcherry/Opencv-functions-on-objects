import cv2
import numpy as np


def feature():
  img1=cv2.imread("./venv/imgs/18.jpg",cv2.IMREAD_GRAYSCALE)
  img2=cv2.imread("./venv/imgs/19.jpg",cv2.IMREAD_GRAYSCALE)

  orb=cv2.ORB_create(nfeatures=1500)
  key1,des1=orb.detectAndCompute(img1,None)
  key2,des2=orb.detectAndCompute(img2,None)
  img1=cv2.drawKeypoints(img1,key1,None)
  img2=cv2.drawKeypoints(img2,key2,None)
  #brute force matching
  bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
  matches=bf.match(des1,des2)
  matches=sorted(matches,key= lambda x:x.distance)
  matching=cv2.drawMatches(img1,key1,img2,key2,matches[:50],None,flags=2)
  cv2.imshow("result",matching)


  cv2.imshow("img1",img1)
  cv2.imshow("img2",img2)
  cv2.waitKey(0)
  cv2.destroyAllWindows()