from __future__ import unicode_literals
#visual
import numpy as np
import cv2
import time
from PIL import Image, ImageFont, ImageDraw
#music

import librosa
import os
from pygame import mixer  # Load the popular external library
from mutagen import mp3
import youtube_dl
import pygame
import sys

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
kernel = np.ones((21, 21), 'uint8')
start_time = time.time()
more_shapes = False
counter = 0

def background(frame, image_name):
    rows,cols,channels = frame.shape
    img1 = cv2.imread(image_name)
    resized_image = cv2.resize(img1, (cols, rows))
    return resized_image

def add_images(frame, image_name):
    frame = cv2.Canny(frame, 50, 100)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    blue, green, red = cv2.split(frame)
    frame = cv2.add(frame, image_name)
    return frame

def play_song(file_name):
    song_file = 'cotton_eye_joe.mp3'
    mp_3 = mp3.MP3(song_file)
    mixer.init(frequency=mp_3.info.sample_rate)
    mixer.music.load(song_file)
    mixer.music.play()


play_song('cotton_eye_joe')
song_start_time = time.time()
tempo = 469
img_1 = np.zeros([512,512,1],dtype=np.uint8)
img_1.fill(255)


while True:

    #Capturing frames from the video feed
    ret, frame = cap.read()
    song_elapsed_time = time.time()-song_start_time
    if song_elapsed_time % tempo == 0:
        cv2.imshow('DREAM TIME MACHINE', img_1)



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

    #Adding background image
    if counter >= 0 and counter < 10:
        resized_image = background(frame, 'frames/000'+str(counter)+'.jpg')
        counter += 1
    elif counter >= 10 and counter < 100:
        resized_image = background(frame, 'frames/00'+str(counter)+'.jpg')
        counter += 1
    elif counter >= 100 and counter < 139:
        resized_image = background(frame, 'frames/0'+str(counter)+'.jpg')
        counter += 1
    else:
        resized_image = background(frame, 'frames/0'+str(counter)+'.jpg')
        counter = 0
    frame = add_images(frame, resized_image)

    #Showing everything
    cv2.imshow('DREAM TIME MACHINE', frame)

    #Stopping everything when key 'q' is hit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Close the window
cap.release()
cv2.destroyAllWindows()
