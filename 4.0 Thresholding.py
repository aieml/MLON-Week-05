import cv2

img=cv2.imread('Samples 1/threshold.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh1=cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(gray,200,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(gray,200,255,cv2.THRESH_TOZERO)
ret,thresh4=cv2.threshold(gray,100,255,cv2.THRESH_TRUNC)

cv2.imshow('IMG',img)
cv2.imshow('THRESH_BIN',thresh1)
cv2.imshow('THRESH_INV',thresh2)
cv2.imshow('THRESH_TOZER',thresh3)
cv2.imshow('THRESH_TRUNC',thresh4)
