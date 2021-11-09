import cv2 as cv

img = cv.imread('demo.jpg')
cv.imshow('Cats', img)

cv.waitKey(0)