# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 13:03:32 2022

@author: Amol
"""

import cv2
img=cv2.imread("birds.jpg")

gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inverted_img=255-gray_img

blurred=cv2.GaussianBlur(inverted_img, (21,21), 0)
inverted_blur=255-blurred

pencil_sketch = cv2.divide(gray_img, inverted_blur, scale=255.0)

cv2.imshow("Original Image", img)
cv2.imshow("Pencil Sketch", pencil_sketch)
cv2.waitKey(0)