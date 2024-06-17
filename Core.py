import requests
from ultralytics import YOLO
import numpy as np
import cv2 as cv
from SuperFunctions import *
import matplotlib.pyplot as plt
Downloads()
#Read Images
imgx1=cv.imread("Limg.jpg")
imgx2=cv.imread("Rimg.jpg")
#Predictmodel
model = YOLO("yolov8n.pt")
results1 = model.predict(imgx1,conf=0.1)
Name1,Markings1=DetectClasses(results1)
results2 = model.predict(imgx2,conf=0.1)
Name2,Markings2=DetectClasses(results2)
#End Result
print(Name1,Markings1)
cen1=(Markings1[0][0],Markings1[0][1])
cen2=(Markings2[0][0],Markings2[0][1])
cen11=(Markings1[0][2],Markings1[0][3])
cen22=(Markings2[0][2],Markings2[0][3])
Rad1=((cen1[0]+cen11[0])//2,(cen1[1]+cen11[1])//2)
Rad2=((cen2[0]+cen22[0])//2,(cen2[1]+cen22[1])//2)
print(cen1[0],cen2[0])
#Estimation of Depth
Focal=1450
Centre=640
abs1=cen1[0]
abs2=cen2[0]
Disparity=abs1-abs2
Distance=abs((Focal*4.5)/Disparity)
print("DistL : ",abs1)
print("DistR : ",abs2)
print("Distance : ",round(Distance,2))
#Marking the Important Things
imgx1=cv.rectangle(imgx1,pt1=cen1,pt2=cen11,color=(0,0,255),thickness=1)
imgx1=cv.putText(imgx1, Name1[0], (Markings1[0][0]+3,Markings1[0][1]-5), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
imgx1=cv.circle(imgx1,center=Rad1,radius=3,color=(0,255,0),thickness=-1)
imgx1=cv.putText(imgx1, "Distance {}".format(round(Distance,2)), (1000,80), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
print(Name2,Markings2)
imgx2=cv.rectangle(imgx2,pt1=cen2,pt2=cen22,color=(0,0,255),thickness=1)
imgx2=cv.putText(imgx2, Name1[0], (Markings2[0][0]+3,Markings2[0][1]-5), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
imgx2=cv.circle(imgx2,center=Rad2,radius=3,color=(0,255,0),thickness=-1)
imgx2=cv.putText(imgx2, "Distance {}".format(round(Distance,2)), (1000,80), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#ShowPoints
imgx1=cv.resize(imgx1,(imgx1.shape[1]//2,imgx1.shape[0]//2))
imgx2=cv.resize(imgx2,(imgx2.shape[1]//2,imgx2.shape[0]//2))
ReCombined = np.vstack((imgx1, imgx2))
cv.imshow("Result", ReCombined)
cv.waitKey(0)
cv.destroyAllWindows()
