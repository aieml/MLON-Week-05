import cv2

img=cv2.imread('Samples 2/gray_image.png')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray,50,255,cv2.THRESH_BINARY)

_,contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:

    cv2.drawContours(img,[cnt],1,(0,255,0),2)

cv2.imshow('IMG',img)
cv2.imshow('THRSH',thresh)
