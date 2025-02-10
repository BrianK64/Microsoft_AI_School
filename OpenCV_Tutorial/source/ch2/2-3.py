import cv2 as cv
import sys

img = cv.imread("OpenCV_Tutorial\source\ch2\soccer.jpg")

if img is None:
    sys.exit("Fild not found")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_small = cv.resize(gray, dsize = (0, 0), fx = 0.5, fy = 0.5)

cv.imwrite("OpenCV_Tutorial\source\ch2\soccer_gray.jpg", gray)
cv.imwrite("OpenCV_Tutorial\source\ch2\soccer_gray_small.jpg", gray_small)

cv.imshow("Color image", img)
cv.imshow("Gray image", gray)
cv.imshow("Gray image small", gray_small)

cv.waitKey()
cv.destroyAllWindows()
