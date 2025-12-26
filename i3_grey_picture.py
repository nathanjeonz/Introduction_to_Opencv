import cv2

cap =cv2.VideoCapture(0)
print("cap passed",cap)

while True:
    r,f = cap.read()
    f1 = cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
    cv2.imshow('webcam',f1)


    key = cv2.waitKey(1)

    if key ==ord('q'):
        break

print('started')




cap.release()
cv2.destroyAllWindows()