## StereoVision
Calibration and Depth Map Generation for Active and Passive Stereo Vision Systems.
## Code Sections 
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

