import cv2
import os
import os.path

path = './img/sain.png'
print(path)

src = cv2.imread(path)

gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
tree = src.copy()

contours, hierarchy = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    src = cv2.drawContours(src, [contour], -1, (0, 255, 0), 2)

contour,hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
for contour in contours:
    tree = cv2.drawContours(tree, [contour], -1, (0, 255, 0), 2)


cv2.imshow('ext', src)
cv2.imshow('tree', tree)


cv2.waitKey()
cv2.destroyAllWindows()