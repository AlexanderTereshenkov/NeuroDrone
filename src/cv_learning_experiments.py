import cv2
import os

img = cv2.imread("img\cat.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Cat", img)
key = cv2.waitKey(0)
print(key)
print(ord("l"))
