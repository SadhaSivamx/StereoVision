### StereoVision
Calibration and Depth Map Generation for Active and Passive Stereo Vision Systems.
### CodeSections 
```text
StereoVision
│
├── /calibration
│   ├── CameraCalibration.py       # Intrinsic/Extrinsic Camera Calibration
│   └── PerspectiveTransform.py    # Image Rectification & Transformation
│
├── /Stereo 
│   ├── SuperFunctions.py         # Detection using YOLO
│   ├── Example.py                # Focal estimation with Known Objects
│   └── Main.py                   # Dense estimation via Disparity
│
├── /Binocular
│   ├── Main.py                   # Control and Depth Estimation
│   └── servo.txt                 # Active Vision: Servo control for camera rig
│
├── /StereoMap
│   ├── Output                    # Results Obtained
│   ├── DepthMap.py               # Template Matching and Map generation
│   └── FocalCode.py              # Focal length from Projection
|
├── license.md                    # License
└── README.md
```
### Steps Involved End to End 
<br>
<img width="1034" height="589" alt="image" src="https://github.com/user-attachments/assets/dabb0c96-eedf-41f7-99fe-663c0a778a80" />
<br>

### Resources & References

**Math & Linear Algebra**
<br>
Essential for understanding the matrix operations used in calibration.
1. [Essence of Linear Algebra (3Blue1Brown)](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) - *Visualizing linear transformations.*
2. [The Matrix Transpose: Visual Intuition](https://www.youtube.com/watch?v=wjYpzkQoyD8) - *Understanding how matrices flip/rotate data.*

<br>

**Calibration & Stereo Vision**
<br>
Core concepts and practical implementation guides.
1. [Simple Stereo | Camera Calibration](https://www.youtube.com/watch?v=hUVyDabn1Mg) - *First Principles of Computer Vision.*
2. [ESP32 Stereo Camera for Distance Estimation](https://www.youtube.com/watch?v=CAVYHlFGpaw) - *Hardware implementation example.*
3. [Depth Estimation with OpenCV Python](https://www.youtube.com/watch?v=uKDAVcSaNZA) - *Code walkthrough for 3D object detection.*

