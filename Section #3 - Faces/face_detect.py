#pylint:disable=no-member

import cv2 as cv

img = cv.imread('../Resources/Photos/group 1.jpg')
cv.imshow('Group of 5 people', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray People', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)



cv.waitKey(0)


[------------------------------------------------------------]
#for video detection

import cv2 as c


cap = c.VideoCapture(0)

harr = c.CascadeClassifier('haar_face.xml')
while True:
    isT, frame = cap.read()

    gray  = c.cvtColor(frame,c.COLOR_RGB2GRAY)
    
    face = harr.detectMultiScale(gray,scaleFactor=1.9,minNeighbors=1)

    for x,y,w,h in face:
        c.rectangle(frame,(x,y),(x+w,y+h),(222,222,222),thickness=2)

        r = gray[y:y+h,x:x+w]
        rc = frame[y:y+h,x:x+w]

    c.imshow('v', frame)
   

    if(c.waitKey(2) & 0xFF == ord('d')):
        break

cap.release()

c.destroyAllWindows()
