'''
    Test the classifier
'''
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('./output/cascade.xml')
# face_cascade = cv2.CascadeClassifier('./output/haarcascade_frontalface_default.xml')


img = cv2.imread('./test_img_set/big_masters.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(gray, 1.3, 5)


for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

