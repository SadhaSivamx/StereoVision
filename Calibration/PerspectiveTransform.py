import cv2 as cv
import numpy as np


rcords = np.float32([
    [0, 0],      # Top-Left
    [0, 400],    # Bottom-Left
    [500, 400],  # Bottom-Right
    [500, 0]     # Top-Right
])

points = []


def Solver(imgpoints, expectedpoints):
    A = []
    B = []

    for i in range(4):
        imgx, imgy = imgpoints[i][0], imgpoints[i][1]
        resx, resy = expectedpoints[i][0], expectedpoints[i][1]
        A.append([imgx, imgy, 1, 0, 0, 0, -imgx * resx, -imgy * resx])
        A.append([0, 0, 0, imgx, imgy, 1, -imgx * resy, -imgy * resy])

        B.append(resx)
        B.append(resy)

    A = np.array(A)
    B = np.array(B)

    try:
        r = np.linalg.solve(A, B)
        matrix = np.append(r, 1)
        return matrix.reshape(3, 3)
    except np.linalg.LinAlgError:
        print("Singular Matrix! Points might be collinear.")
        return np.eye(3)


def clickevent(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        if len(points) < 4:
            points.append([x, y])
            cv.circle(params['img'], (x, y), 5, (0, 255, 0), -1)
            cv.imshow('Freeze Frame', params['img'])
            print(f"Point selected: {x}, {y}")


cap = cv.VideoCapture(0)

print("Press 'f' to FREEZE the frame and select points.")

while True:
    ret, frame = cap.read()
    if not ret: break

    cv.imshow('Video', frame)

    if cv.waitKey(1) & 0xFF == ord('f'):
        img = frame.copy()
        cv.imshow('Freeze Frame', img)
        cv.setMouseCallback('Freeze Frame', clickevent, {'img': img})

        print('''
        Please click 4 points in this order : 
        Top-Left, Bottom-Left, Bottom-Right, Top-Right
        ''')

        cv.waitKey(0)
        break

cap.release()
cv.destroyAllWindows()

if len(points) == 4:
    print("------------------------------------------")
    print("We have obtained the Homography matrix...")

    # Run the solver
    Matrix = Solver(imgpoints=points, expectedpoints=rcords)

    print("\nCalculated Matrix:")
    print(np.round(Matrix, 3))

    warped_img = cv.warpPerspective(img, Matrix, (500, 400))

    cv.imshow("Original Freeze", img)
    cv.imshow("Warped Result", warped_img)

    print("\nPress any key to exit...")
    cv.waitKey(0)

cv.destroyAllWindows()