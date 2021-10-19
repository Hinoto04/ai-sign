import cv2
import numpy as np
from scipy.spatial import distance as dist

def label(image, contour):


   mask = np.zeros(image.shape[:2], dtype="uint8")
   cv2.drawContours(mask, [contour], -1, 255, -1)

   mask = cv2.erode(mask, None, iterations=2)
   mean = cv2.mean(image, mask=mask)[:3]


   minDist = (np.inf, None)



   for (i, row) in enumerate(lab):

       d = dist.euclidean(row[0], mean)

       if d < minDist[0]:
           minDist = (d, i)

   return colorNames[minDist[1]]

colors = [[0, 0, 255], [0, 255, 0], [255, 0, 0]]
colorNames = ["red", "green", "blue"]



lab = np.zeros((len(colors), 1, 3), dtype="uint8")
for i in range(len(colors)):
   lab[i] = colors[i]

lab = cv2.cvtColor(lab, cv2.COLOR_BGR2LAB)

path = './img/Jsain.png'
image = cv2.imread(path, 1)


blurred = cv2.GaussianBlur(image, (5, 5), 0)

gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)

img_lab = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)

thresh = cv2.erode(thresh, None, iterations=2)
cv2.imshow("Thresh", thresh)


contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


if len(contours) == 2:
   contours = contours[0]

elif len(contours) == 3:
   contours = contours[1]


for contour in contours:

   cv2.imshow("Image", image)
   cv2.waitKey(0)


   cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)


   color_text = label(img_lab, contour)
   setLabel(image, color_text, contour)


cv2.imshow("Image", image)
cv2.waitKey(0)

