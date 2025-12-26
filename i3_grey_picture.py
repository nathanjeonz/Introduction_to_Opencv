import cv2

cap =cv2.VideoCapture(0)
print("cap passed",cap)

while True:
    r,f = cap.read()
    cv2.imshow('webcam',f)
    
print('started')




cap.release()
cv2.destroyAllWindows()