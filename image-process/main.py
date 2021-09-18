import cv2
import numpy as np
import os 
try: 
    from PIL import Image 
except ImportError: 
    import Image 
import pytesseract

capture = cv2.VideoCapture(0)                        #카메라 설정
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 600)           
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)

def featureMatching():
    img1 = cv2.imread('기준이될 싸인 주소', cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread('대조할 싸인 주소', cv2.IMREAD_GRAYSCALE)
    res = None

    orb = cv2.ORB_create()
    kp1, des1 =orb.detectAndCompute(img1, None)
    kp2, des2 =orb.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)

    matches = sorted(matches, key=lambda x:x.distance)
    res = cv2.drawMatches(img1, kp1, img2, kp2, matches[:30], res, flags=0)

    cv2.inshow('Feature Mathhing', res)

featureMatching()
# gray = cv2.cvtColor(capture, cv2.COLOR_RGB2GRAY)         #윤곽선 검출
# ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# binary = cv2.bitwise_not(binary)

# contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

# for i in range(len(contours)):
#     cv2.drawContours(capture, [contours[i]], 0, (0, 0, 255), 2)
#     cv2.putText(capture, str(i), tuple(contours[i][0][0]), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
#     print(i, hierarchy[0][i])
#     cv2.imshow("capture", capture)
#     cv2.waitKey(0)

# 설치한 tesseract 프로그램 경로 (64비트) 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract' 
# 이미지 불러오기, Gray 프로세싱 
gray = cv2.cvtColor(capture, cv2.COLOR_BGR2GRAY)
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)
 # Simple image to string 
text = pytesseract.image_to_string(Image.open(filename), lang=None)
os.remove(filename)

print(text)

cv2.imshow("capture", capture)
cv2.waitKey(0)
cv2.destroyAllWindows()

