import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('Images/rimg.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('Images/limg.jpg', cv2.IMREAD_GRAYSCALE)
img1 = cv2.resize(img1, (img1.shape[1] // 6, img1.shape[0] // 6))
img2 = cv2.resize(img2, (img2.shape[1] // 6, img2.shape[0] // 6))
img2cpy=img2.copy()

sift = cv2.SIFT_create()

kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
matches = bf.match(des1, des2)

matches = sorted(matches, key=lambda x: x.distance)

y_offsets = []
for match in matches:
    pt1 = kp1[match.queryIdx].pt
    pt2 = kp2[match.trainIdx].pt
    y_offsets.append(pt1[1] - pt2[1])

y_offset = int(np.mean(y_offsets))
print(f"y-offset: {y_offset}")

M = np.float32([[1, 0, 0],[0, 1, y_offset]])
aligned_img = cv2.warpAffine(img2, M, (img1.shape[1], img1.shape[0]))

img1=img1
img2=aligned_img
kernel=(5,5)
img1 = cv2.GaussianBlur(img1, kernel, 0)
img2 = cv2.GaussianBlur(img2, kernel, 0)


w,h=img1.shape

#From CamCabration
focal_length = 550
baseline = 5
block_size = 15

ze=np.zeros((w,h))
disparity_map = np.zeros_like(img1, dtype=np.float32)
def TemplateMatch(template,img):
    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    return max_val,max_loc

for i in range(block_size+10, img1.shape[0] - block_size):
    for j in range(block_size+10, img1.shape[1] - block_size):
        template = img1[i-block_size:i + block_size, j - block_size:j + block_size]
        searcharea = img2[max(0, i-block_size-15):min(i+block_size+15, h), j:]
        try:
            val,pos=TemplateMatch(template,searcharea)
            if pos[0]!=0 and val>0.65:
                distance=int((focal_length*baseline)/(pos[0]))
                if distance > 0 and distance <=255:
                    ze[i][j]=255-distance
                else:
                    ze[i][j]=0
        except:
            pass

fig, axes = plt.subplots(1, 3, figsize=(30, 10))

axes[0].imshow(img1,cmap="gray")
axes[0].set_title('OriL-img')
axes[0].axis('off')

axes[2].imshow(img2cpy,cmap="gray")
axes[2].set_title('OriR-img')
axes[2].axis('off')

axes[1].imshow(ze, cmap='plasma',interpolation="bilinear")
axes[1].set_title('DepthImage')
axes[1].axis('off')

plt.tight_layout()
plt.show()