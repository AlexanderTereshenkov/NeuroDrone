import cv2
import os

img = cv2.imread("img\cat.jpg", cv2.IMREAD_GRAYSCALE)
print(img.shape)
cv2.waitKey(0)
