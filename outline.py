import numpy as np
import cv2
import time
from PIL import Image, ImageFont, ImageDraw

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
kernel = np.ones((21, 21), 'uint8')
start_time = time.time()
more_shapes = False

while True:

    #Capturing frames from the video feed
    ret, frame = cap.read()

    #Drawing pulsing circles from each detected face
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20, 20))
    for (x, y, w, h) in faces:
        elapsed_time = time.time()-start_time
        print(elapsed_time)
        cv2.circle(frame, (x+2*int(w/4), y+int(h/3)),int(w/20)*int(300**elapsed_time), (255,255,255), thickness=1, lineType=8, shift=0)
        if more_shapes == True:
            start_time = time.time()
            more_shapes = False
        if elapsed_time > 0.75:
            start_time = time.time()
            more_shapes = True

    #Making the background blue
    frame = cv2.Canny(frame, 50, 100)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    blue, green, red = cv2.split(frame)
    frame = cv2.add(frame, 50)

    #Showing everything
    cv2.imshow('DREAM TIME MACHINE', frame)

    #Stopping everything when key 'q' is hit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Close the window
cap.release()
cv2.destroyAllWindows()
