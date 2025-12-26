import cv2
print("started")

cap = cv2.VideoCapture(0)
print("cap passed",cap)

while True:
    ret, frame = cap.read() # reading camera # this os 
    cv2.imshow("webcam",frame) # showing camera output

    key = cv2.waitKey(1) & 0xFF # reading key

    # space key is 32
    if key ==32:
        cv2.imwrite("photo.jpg",frame)
        print("phto is saved!")

    if key ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
