import cv2 as cv
import numpy as np
from scipy.linalg import rq


L, W, H = 9.8, 4.5, 5.0

obj_pts = np.float32([
    [0, 0, 0],  # Point 1: Front-Left-Bottom
    [L, 0, 0],  # Point 2: Front-Right-Bottom
    [0, 0, H],  # Point 3: Front-Left-Top
    [L, 0, H],  # Point 4: Front-Right-Top
    [L, W, 0],  # Point 5: Back-Right-Bottom
    [L, W, H]   # Point 6: Back-Right-Top
])

points_2d = []


def solve_p_matrix(obj_points, img_points):
    A = []
    for i in range(len(obj_points)):
        X, Y, Z = obj_points[i]
        u, v = img_points[i]

        A.append([X, Y, Z, 1, 0, 0, 0, 0, -u * X, -u * Y, -u * Z, -u])
        A.append([0, 0, 0, 0, X, Y, Z, 1, -v * X, -v * Y, -v * Z, -v])

    A = np.array(A)

    _, _, Vh = np.linalg.svd(A)
    L_vector = Vh[-1, :]

    return L_vector.reshape(3, 4)


def decompose_projection(P):

    M = P[:, :3]
    h = P[:, 3]

    K, R = rq(M)

    T = np.diag(np.sign(np.diag(K)))
    K = K @ T
    R = T @ R
    
    scale_factor = K[2, 2]
    K = K / scale_factor
    h = h / scale_factor
    
    t = np.linalg.inv(K) @ h

    return K, R, t


def click_event(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        if len(points_2d) < 6:
            points_2d.append([x, y])
            cv.circle(params['img'], (x, y), 5, (0, 255, 0), -1)
            cv.putText(params['img'], str(len(points_2d)), (x + 10, y),
                       cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv.imshow('Selection', params['img'])
            print(f"Captured Point {len(points_2d)}: ({x}, {y})")


# --- MAIN EXECUTION ---
cap = cv.VideoCapture(0)
print("Press 'f' to freeze and select 6 points in order 1 to 6.")

while True:
    ret, frame = cap.read()
    if not ret: break
    cv.imshow('Live Feed', frame)
    if cv.waitKey(1) & 0xFF == ord('f'):
        img = frame.copy()
        cv.imshow('Selection', img)
        cv.setMouseCallback('Selection', click_event, {'img': img})
        cv.waitKey(0)
        break

cap.release()
cv.destroyAllWindows()

if len(points_2d) == 6:
    P = solve_p_matrix(obj_pts, np.array(points_2d))

    K, R, t = decompose_projection(P)

    print("\n--- Calibration Results ---")
    print("Intrinsic Matrix (K):\n", np.round(K, 2))
    print("\nRotation Matrix (R):\n", np.round(R, 2))
    print("\nTranslation Vector (t):\n", np.round(t, 2))

    axis_3d = np.float32([[0, 0, 0], [5, 0, 0], [0, 5, 0], [0, 0, 5]])
    axis_2d = []

    for p3d in axis_3d:
        p_homog = P @ np.append(p3d, 1)
        u = p_homog[0] / p_homog[2]
        v = p_homog[1] / p_homog[2]
        axis_2d.append((int(u), int(v)))

    origin = axis_2d[0]
    cv.line(img, origin, axis_2d[1], (0, 0, 255), 3)  # X - Red
    cv.line(img, origin, axis_2d[2], (0, 255, 0), 3)  # Y - Green
    cv.line(img, origin, axis_2d[3], (255, 0, 0), 3)  # Z - Blue

    cv.imshow("Pose Estimation - 3D Axes", img)
    cv.waitKey(0)

if len(points_2d) == 6:
    P = solve_p_matrix(obj_pts, np.array(points_2d))

    K, R, t = decompose_projection(P)
    K = K / K[2, 2]

    t_column = t.reshape(3, 1)
    Extrinsic = np.hstack((R, t_column))

    print("\n" + "=" * 30)
    print("      CAMERA PARAMETERS")
    print("=" * 30)

    print("\n[1] INTRINSIC MATRIX (K)")
    print("Format: [[fx, s, cx], [0, fy, cy], [0, 0, 1]]")
    print(np.round(K, 3))

    print("\n[2] EXTRINSIC MATRIX [R | t]")
    print("Dim: 3x4 (Rotation | Translation)")
    print(np.round(Extrinsic, 3))

    print("\n[3] CAMERA POSE DETAILS")
    print(f"Focal Length (X): {K[0, 0]:.2f} px")
    print(f"Focal Length (Y): {K[1, 1]:.2f} px")
    print(f"Principal Point: ({K[0, 2]:.2f}, {K[1, 2]:.2f})")
    print(f"Distance to Object: {np.linalg.norm(t):.2f} units")
    print("=" * 30)



cv.destroyAllWindows()
