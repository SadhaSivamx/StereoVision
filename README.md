### StereoVision
Calibration and Depth Map Generation for Active and Passive Stereo Vision Systems.
### CodeSections 
```text
/Stereo-Vision-Project
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
### Resources & References
<br>
Math ( linear algebra ) :
<br>
1. [Essence of Linear Algebra ](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
2. [Matrix Transpose](https://www.youtube.com/watch?v=wjYpzkQoyD8)
<br>
Calibration and Stereo :
<br>
1. [Simple Stereo | Camera Calibration](https://www.youtube.com/watch?v=hUVyDabn1Mg)
2. [ESP32 stereo camera for object detection, recognition and distance estimation](https://www.youtube.com/watch?v=CAVYHlFGpaw)
3. [Depth Estimation with OpenCV Python for 3D Object Detection](https://www.youtube.com/watch?v=uKDAVcSaNZA)

