import cv2
c = cv2.VideoCapture(0)
print("cap passed",c)

face = cv2.CascadeClassifier("apple.xml")

while True:
    r,t = c.read()
    cv2.imshow("web",t)

    faces = face.detectMultiScale(t,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(t,(x,y),(x+w,y+h),(0,255,0),2)



    k = cv2.waitKey(1)

    if k ==ord('q'):
        break
c.release()
cv2.destroyAllWindows()