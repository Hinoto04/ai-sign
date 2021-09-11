import cv2

capture = cv2.VideoCapture(0)                        #카메라 설정
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 600)           
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)

gray = cv2.cvtColor(capture, cv2.COLOR_RGB2GRAY)         #윤곽선 검출
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
binary = cv2.bitwise_not(binary)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

for i in range(len(contours)):
    cv2.drawContours(capture, [contours[i]], 0, (0, 0, 255), 2)
    cv2.putText(capture, str(i), tuple(contours[i][0][0]), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
    print(i, hierarchy[0][i])
    cv2.imshow("capture", capture)
    cv2.waitKey(0)
