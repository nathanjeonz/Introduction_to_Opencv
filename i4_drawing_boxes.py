import cv2
c = cv2.VideoCapture(0)
print("cap passed",c)

face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    r,t = c.read()
    
    gray = cv2.cvtColor(t,cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray,1.3,5)
    print(faces)

    for (x,y,w,h) in faces:
        cv2.rectangle(t,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("web",t)

    k = cv2.waitKey(1)

    if k ==ord('q'):
        break
c.release()
cv2.destroyAllWindows()