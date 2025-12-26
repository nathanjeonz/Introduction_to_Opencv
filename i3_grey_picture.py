import cv2
print('started')

cap =cv2.VideoCapture(0)
print("cap passed",cap)

while True:
    r,f = cap.read()
    cv2.imshow('webcam',f)

    



cap.release()
cv2.destroyAllWindows()