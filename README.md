## StereoVision
stereovision with esp32 cams for depth estimation , using Yolo , Opencv etc 
## References
1. [ESP32 stereo camera for object detection, recognition and distance estimation](https://www.youtube.com/watch?v=CAVYHlFGpaw)
2. [Depth Estimation with OpenCV Python for 3D Object Detection](https://www.youtube.com/watch?v=uKDAVcSaNZA)
## Steps Involved
1. Capturing Images
2. Spotting the Centre Point
3. Setting Up focal Length
4. Calculation of Disparity
5. Calculation of Image Depth
## Diagram for Problem Approach
![Screenshot 2024-06-17 125612](https://github.com/SadhaSivamx/StereoVision/assets/106687593/d229f085-0521-4db5-b903-f3ad643786d8)
## Output
![Esp32-StereoVision](https://github.com/SadhaSivamx/StereoVision/assets/106687593/b9ba9b04-ea1c-4d95-b157-046450cbd087)
## StereoMap Generation
the Above Process is done for every pixel and the depthmap is generated
## References
1. [Simple Stereo | Camera Calibration](https://www.youtube.com/watch?v=hUVyDabn1Mg)
## Output
![DepthMap](https://github.com/user-attachments/assets/00ced0c9-b74e-4406-a1df-9be825a04e7e)
## Active Binocular vision system
In this Active Binocular Vision System, the traditional static base is replaced with a servo-controlled mechanism.
The system achieves convergence by adjusting the servos to center the target in both camera images.

This mechanical convergence forms two geometric triangles.By solving the equations derived from the 
servo angles, the system calculates the exact depth ($Z$) of the object relative to the baseline.

## Diagram for Problem Approach
<img width="714" height="531" alt="image" src="https://github.com/user-attachments/assets/bef6c1d9-e222-42c4-8d49-9a8cd9e54421" />

## Output
https://github.com/user-attachments/assets/2603df8d-184a-4ad2-aa12-cd7809b3de5b

