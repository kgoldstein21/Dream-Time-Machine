"play Deep Dream Video"

import cv2
import numpy as np


time_speed = 10
# cap = cv2.VideoCapture('VIDEO')
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()


    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(time_speed) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
