import cv2, sys
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import os
import os.path
import copy

path = './img/sain.png'
image = cv2.imread(path)
image_gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

des = cv2.bitwise_not(image_gray)
contour,hier = cv2.findContours(des,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contour:
    cv2.drawContours(des,[cnt],0,255,-1)

gray = cv2.bitwise_not(des)

cv2.imshow('Edged', gray)
cv2.waitKey(0)

cv2.destroyAllWindows()

# r.save("D:/temp/pika_rev.png")























































# import cv2
# import os
# import os.path

# path = './img/insa.png'
# print(path)

# src = cv2.imread(path)

# gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
# tree = src.copy()

# contours, hierarchy = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# for contour in contours:
#     src = cv2.drawContours(src, [contour], -1, (0, 255, 0), 2)

# contour,hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# for contour in contours:
#     tree = cv2.drawContours(tree, [contour], -1, (0, 255, 0), 2)


# cv2.imshow('ext', src)
# cv2.imshow('tree', tree)


# cv2.waitKey()
# cv2.destroyAllWindows()
