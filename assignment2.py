import cv2
import numpy as np

image = cv2.imread(r'img1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (29,837), 0)
thresh = cv2.threshold(blur, 0, 245, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
rows, cols = thresh.shape
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25,25))

dilate = cv2.dilate(thresh, kernel, iterations=10)
count=0
# Find contours and draw rectangle
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(len(cnts))
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    if(((y+h)-y)==rows):
        count+=1
for i in range(count-1):
    X = (i+1)*cols//count
    cv2.line(image, (X,rows//15),(X,rows-25), (255,0,0), 2)
cv2.imshow('image', image)
if cv2.waitKey(0):
    cv2.destroyAllWindows()
