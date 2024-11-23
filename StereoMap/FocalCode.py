import cv2
import numpy as np

# read image
img1 = cv2.imread("Images/lg.jpg")
img2 = cv2.imread("Images/rg.jpg")
foc = cv2.imread("Images/fc.jpg")
imgx1 = cv2.resize(img1, (img1.shape[1] // 6, img1.shape[0] // 6))
imgx2 = cv2.resize(img2, (img1.shape[1] // 6, img1.shape[0] // 6))
focx = cv2.resize(foc, (img1.shape[1] // 6, img1.shape[0] // 6))
disp = np.hstack((imgx1, imgx2))
# show image
cv2.imshow('image', focx)
# focal length estimation
ytoy = []
# define the events for the
# mouse_click.
counter1 = 1


def focalcalc(event, x, y, flags, param):
    global counter1
    if event == cv2.EVENT_LBUTTONDOWN:
        if counter1 <= 2:
            ytoy.append(x)
            counter1 = counter1 + 1
            cv2.imshow('image', focx)

        else:
            cv2.destroyAllWindows()


cv2.setMouseCallback('image', focalcalc)
cv2.waitKey(0)

y1 = ytoy[0]
y2 = ytoy[1]
smallw = y1 - y2
capw = 1
d = 10
focal = (d * smallw) / capw
print("focal length: ", focal)
# PART2
cv2.imshow('image', disp)

coord = []

counter2 = 1


def mouse_click(event, x, y, flags, param):
    global counter2
    if event == cv2.EVENT_LBUTTONDOWN:
        if counter2 <= 2:
            print(x - (img1.shape[1] // 6) * (counter2 - 1), " ", y)
            coord.append(x - (img1.shape[1] // 6) * (counter2 - 1))
            counter2 = counter2 + 1
            cv2.circle(disp, (x, y), 10, (255, 255, 0), 2)
            cv2.imshow('image', disp)
        else:
            cv2.destroyAllWindows()


cv2.setMouseCallback('image', mouse_click)
cv2.waitKey(0)

baseline = 5
abs1 = coord[0]
abs2 = coord[1]
disparity = abs1 - abs2
distance = abs((focal * baseline) / disparity)
print("distance: ", distance)

# close all the opened windows.
cv2.destroyAllWindows()