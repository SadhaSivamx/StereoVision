import serial
import numpy as np
import cv2 as cv
import time

#i have connected it in COM6 ( need to be changed as per the connection )
ser = serial.Serial("COM6", 9600, timeout=1)
time.sleep(1)

#cam inits ( cam 0,2 needs to be changed )
cap0 = cv.VideoCapture(0, cv.CAP_DSHOW)
cap1 = cv.VideoCapture(2, cv.CAP_DSHOW)

#centrex
width = 640
Cx = width // 2
Limit = 20

ps1=None
ps2=None

#cmd the servo
def speak2servo(a1, a2):
    cmd = f"M1:{a1},M2:{a2}\n"
    ser.write(cmd.encode())
    time.sleep(0.03)

#left and right search start
servo1 = 45
servo2 = 135

#yellow Declaration
ly = np.array([20, 100, 100])
uy = np.array([35, 255, 255])
kernel = np.ones((5, 5), np.uint8)

#finding centre
def centerx(frame):
    #hsv for accurate processing
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    #mask creationg
    mask=cv.inRange(hsv, ly, uy)

    #mask from opertions
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)

    #contors
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    if not contours:
        return None, mask, None

    #get area within 250 units
    c = max(contours, key=cv.contourArea)
    if cv.contourArea(c) < 250:
        return None, mask, None

    #capture centre
    x, y, w, h = cv.boundingRect(c)

    M = cv.moments(c)
    if M["m00"] == 0:
        return None, mask, None

    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])
    return cx, mask, (x, y, w, h, cx, cy)

speak2servo(servo1,servo2)
time.sleep(1)
print("Starting Operations")

while True:
    ret0, frame0 = cap0.read()
    ret1, frame1 = cap1.read()

    if not ret0 or not ret1:
        break

    cx0, mask0, infox1 = centerx(frame0)
    cx1, mask1, infox2 = centerx(frame1)

    if cx0 is None:
        servo2-=1
    else:
        x, y, w, h, cx, cy = infox1
        cv.rectangle(frame0, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.circle(frame0, (cx, cy), 5, (0, 0, 255), -1)
        cv.putText(frame0, f"({cx},{cy})", (cx + 5, cy - 5),cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

        error=Cx-cx0
        cv.putText(frame0, f"Err: {error}", (10, 30),cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
        if error not in range(-Limit,+Limit):
            dir=(1 if error>0 else -1)
            servo2+=dir

    if cx1 is None:
        servo1+=1
    else:
        x, y, w, h, cx, cy = infox2
        cv.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.circle(frame1, (cx, cy), 5, (0, 0, 255), -1)
        cv.putText(frame1, f"({cx},{cy})", (cx + 5, cy - 5), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

        error=Cx-cx1
        cv.putText(frame1, f"Err: {error}", (10, 30),cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
        if error not in range(-Limit,+Limit):
            dir=(1 if error>0 else -1)
            servo1+=dir
    #qqprint("ang:{},{} uts".format(servo1,servo2))
    speak2servo(servo1, servo2)

    cv.line(frame0, (Cx, 0), (Cx, frame0.shape[0]), (255, 0, 0), 1)
    cv.line(frame1, (Cx, 0), (Cx, frame1.shape[0]), (255, 0, 0), 1)

    if ps1==servo1 and ps2==servo2:
        #print("Convergence is Done.....")

        alpha = servo1 - 90
        beta = 90 - servo2

        #angles
        alpha = np.deg2rad(alpha)
        beta = np.deg2rad(beta)
        Baseline=15

        depth = Baseline / (np.tan(alpha) + np.tan(beta))
        #print("Depth Calculated :",round(depth,2),"Cm from Baseline")
        cv.putText(frame0, f"Dist: {round(depth,2)}cm", (10, 80), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 1)
        cv.putText(frame1, f"Dist: {round(depth,2)}cm", (10, 80), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 1)

    ps1,ps2=(servo1,servo2)
    s=1.5
    frame0=cv.resize(frame0,(int(640/s),int(480/s)))
    frame1=cv.resize(frame1,(int(640/s),int(480/s)))
    cv.imshow("Cam 0", frame0)
    cv.imshow("Cam 1", frame1)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(0.2)

cap0.release()
cap1.release()
ser.close()
cv.destroyAllWindows()