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

import ctypes

#initializing video capture and facial recognition variables and setting default mode and song
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 3000)
ret, frame = cap.read()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
kernel = np.ones((21, 21), 'uint8')
start_time = time.time()
more_shapes = False
counter = 0
corpcounter = 0
dir=True
mode="happy"
song="super"

def background(frame, image_name):
    '''
    Takes in a frame image and an image name string.

    Matches the size of the image to the size of the frame.

    Returns the resized image.
    '''
    rows,cols,channels = frame.shape
    img1 = cv2.imread(image_name)
    resized_image = cv2.resize(img1, (cols, rows))
    return resized_image

def add_images(frame, image_name):
    '''
    Takes in a frame image and an image name string.

    Finds outlines in the frame and superimposes those on top of the image belonging to the image name.

    Returns the final composite image.
    '''
    frame = cv2.Canny(frame, 50, 100)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    blue, green, red = cv2.split(frame)
    frame = cv2.add(frame, image_name)
    return frame

def play_song(file_name):
    mp_3 = mp3.MP3(file_name)
    mixer.init(frequency=mp_3.info.sample_rate)
    mixer.music.load(file_name)
    mixer.music.play()

def combinedVisual(cap, face_cascade, kernel, start_time, more_shapes, counter, corpcounter, dir, mode, song):
    '''
    Takes in a video capture, an image cascade, a kernel, a start time, a boolean more_shapes,
    a counter, another counter, a boolean dir, a mode name string, and a song name string.

    Does all the heavy lifting for the video and audio ouput-- plays the selected song, opens
    up a video feed, draws circles over each detected face to the beat of the song, chooses a
    background from the frames_and_modes folder based on the chosen mode, shows everything in a
    window, and then closes everything when you hit the 'q' key.
    '''
    play_song('playlist/'+song+'.mp3')
    song_start_time = time.time()
    tempo = int(603)
    wid = 0
    threshold = tempo

    while True:

        #Capturing frames from the video feed
        ret, frame = cap.read()
        song_elapsed_time = 1000*(time.time()-song_start_time)

        #Drawing pulsing circles from each detected face
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20, 20))
        for (x, y, w, h) in faces:
            elapsed_time = time.time()-start_time
            if song_elapsed_time > threshold:
                threshold += tempo
                if wid < 50:
                    wid += 10
                else:
                    wid = 10
            cv2.circle(frame, (x+2*int(w/4), y+int(h/3)),int(w/20)*int(wid), (255,255,255), thickness=1, lineType=8, shift=0)
            if more_shapes == True:
                start_time = time.time()
                more_shapes = False
            if elapsed_time > 0.75:
                start_time = time.time()
                more_shapes = True


        #Adding background image based on selected mode
        if mode == "corporate":
            if counter >= 0 and counter < 66:
                if corpcounter < 15:
                    print(mode+'/stock'+str(counter)+'.jpg')
                    resized_image = background(frame, 'frames_and_modes/'+mode+'/stock'+str(counter+1)+'.jpg')
                    corpcounter += 1
                    print(corpcounter)
                else:
                    print("counter iterating")
                    counter += 1
                    corpcounter = 0
            else:
                counter = 0
        else:
            if dir == True:
                if counter >= 0 and counter < 10:
                    resized_image = background(frame, 'frames_and_modes/'+mode+'/000'+str(counter)+'.jpg')
                    counter += 1
                elif counter >= 10 and counter < 100:
                    resized_image = background(frame, 'frames_and_modes/'+mode+'/00'+str(counter)+'.jpg')
                    counter += 1
                elif counter >= 100 and counter < 129:
                    resized_image = background(frame, 'frames_and_modes/'+mode+'/0'+str(counter)+'.jpg')
                    counter += 1
                else:
                    resized_image = background(frame, 'frames_and_modes/'+mode+'/0'+str(counter)+'.jpg')
                    dir = False
            elif dir == False:
                if counter <= 129 and counter >= 100:
                    resized_image = background(frame, 'frames_and_modes/'+mode+'/0'+str(counter)+'.jpg')
                    counter -= 1
                elif counter < 100 and counter >= 10:
                    resized_image = background(frame, 'frames_and_modes/'+mode+'/00'+str(counter)+'.jpg')
                    counter -= 1
                elif counter < 10 and counter > 1:
                    resized_image = background(frame, 'frames_and_modes/'+mode+'/000'+str(counter)+'.jpg')
                    counter -= 1
                else:
                    resized_image = background(frame, 'frames_and_modes/'+mode+'/000'+str(counter)+'.jpg')
                    dir = True

        frame = add_images(frame, resized_image)

        cv2.imshow('DREAM TIME MACHINE', frame)

        #Stopping everything when key 'q' is hit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            mixer.music.stop()
            break

    #Close the window
    cap.release()
    cv2.destroyAllWindows()
