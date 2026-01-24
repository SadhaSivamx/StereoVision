import requests
from ultralytics import YOLO
import cv2 as cv
def DetectClasses(results):
    Ans = results[0]
    NUM=[]
    ARR=[]
    Dec=[]
    try:
        liso = list(map(int, Ans.boxes.cls))
        for i in range(len(liso)):
            if liso[i]==0:
                NUM+=["MAN"]
                Dec+=[i]
            elif liso[i] in [3,7]:
                NUM+=["TRUCK"]
                Dec+=[i]
        for _ in Dec:
            box = Ans.boxes[_]
            # Finding Objects Coordinatz
            dim = box.xyxy[0]
            print(dim)
            x, y, w, h = list(map(int, dim))
            ARR.append(list(map(int, dim)))
        return NUM,ARR
    except:
        pass
def Downloads():
    url1 = "http://192.168.171.26/capture"
    url2 = "http://192.168.171.67/capture"

    # Destination filenames
    filename1 = "Rimg.jpg"
    filename2 = "Limg.jpg"

    def download_image(url, filename):
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f"Image downloaded and saved as {filename}")
        else:
            print(f"Failed to download image from {url}")

    # Download the images
    download_image(url1, filename1)
    download_image(url2, filename2)