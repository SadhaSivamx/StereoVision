import cv2 as cv
from SuperFunctions import *

#Finding the Focal Length
imgx1=cv.imread("Limg.jpg")
imgx2=cv.imread("Rimg.jpg")
model = YOLO("yolov8n.pt")
results1 = model.predict(imgx1)
results2 = model.predict(imgx2)
Name1,Markings1=DetectClasses(results1)
Name2,Markings2=DetectClasses(results2)
cen1=(Markings1[0][0],Markings1[0][1])
cen2=(Markings2[0][0],Markings2[0][1])
cen11=(Markings1[0][2],Markings1[0][3])
cen22=(Markings2[0][2],Markings2[0][3])
Rad1=((cen1[0]+cen11[0])//2,(cen1[1]+cen11[1])//2)
Rad2=((cen2[0]+cen22[0])//2,(cen2[1]+cen22[1])//2)
imgx1=cv.rectangle(imgx1,pt1=cen1,pt2=cen11,color=(0,0,255),thickness=1)
imgx1=cv.putText(imgx1, "Truck", (Markings1[0][0]+3,Markings1[0][1]-5), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
imgx1=cv.circle(imgx1,center=Rad1,radius=3,color=(0,255,0),thickness=-1)
PixelWidth=cen11[0]-cen1[0]
Truewidth=8.5
Distance=23
Focal=round((Distance*PixelWidth)/Truewidth,1)
print("Focalenght in Px :",Focal)


#example for Depth
Focal=1450
Centre=640
if cen1[0]>=Centre:
    abs1=Centre-cen1[0]
else:
    abs1=-(Centre-cen1[0])
if cen2[0]>=Centre:
    abs2=Centre-cen2[0]
else:
    abs2=-(Centre-cen2[0])
Disparity=abs1-abs2
Distance=abs((Focal*4.5)/Disparity)
print("Distance : ",round(Distance,2))
cv.imshow("Frame",imgx1)
cv.waitKey(0)
cv.destroyAllWindows()
