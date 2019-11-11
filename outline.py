import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
kernel = np.ones((21, 21), 'uint8')
start_time = time.time()

while True:
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20, 20))
    for (x, y, w, h) in faces:
        elapsed_time = time.time()-start_time
        print(elapsed_time)
        cv2.rectangle(frame, (x+3, y+3), (x+int(2**elapsed_time), y+int(2**elapsed_time)), (0, 0, 255))
    frame = cv2.Canny(frame, 50, 100)
    cv2.imshow('DREAM TIME MACHINE', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
