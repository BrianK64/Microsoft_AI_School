import cv2 as cv
import sys

img = cv.imread("OpenCV_Tutorial\source\ch2\soccer.jpg")

if img is None:
    sys.exit("File not found.")

cv.imshow("Image Display",img)

cv.waitKey()
cv.destroyAllWindows()