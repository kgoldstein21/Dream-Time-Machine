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

    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20, 20))
    for (x, y, w, h) in faces:
        elapsed_time = time.time()-start_time
        cv2.circle(frame, (x+2*int(w/4), y+int(h/3)),int(w/20)*int(300**elapsed_time), (255,255,255), thickness=1, lineType=8, shift=0)
        if more_shapes == True:
            start_time = time.time()
            more_shapes = False
        if elapsed_time > 0.75:
            more_shapes = True
    frame = cv2.Canny(frame, 50, 100)
    # decoded_image = Image.new("RGB", frameSize)
    # pixels = decoded_image.load()
    cv2.imshow('DREAM TIME MACHINE', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
