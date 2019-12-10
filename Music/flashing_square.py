from __future__ import unicode_literals
import numpy as np
import librosa
import os
from pygame import mixer  # Load the popular external library
from mutagen import mp3
import youtube_dl
import pygame
import sys

# --- constants ---

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)

BEAT = pygame.USEREVENT + 1

# --- classes ---

class Rectangle():

    def __init__(self, color, rect, time, delay):
        self.color = color
        self.rect = rect
        self.time = time
        self.delay = delay
        self.show = False

    def draw(self, screen):
        if self.show:
            pygame.draw.rect(screen, self.color, self.rect)

    def update(self, current_time):
        self.show = not self.show


### New stuff for event
    def __event_handle(self):
        for event in pygame.event.get():
            if event.type == BEAT:
                self.update(current_time)



# --- main ---

def main():
    pygame.init()

    fenetre = pygame.display.set_mode((500, 400), 0, 32)

    current_time = pygame.time.get_ticks()

    # time of show or hide
    delay = 500 # 5000ms = 0.5s

    # objects
    #rect_white = Rectangle(WHITE, (200,150,100,50), current_time, 500)
    #rect_red = Rectangle(RED, (100,150,100,50), current_time + 150, 100)
    rect_green = Rectangle(GREEN, (0, 0, 500, 400), current_time + 300, 468.75)

    #beat_times = libro('cotton_eye_joe')
    #beat = 0
    #beat_time = beat_times[0]
    #time_check = 1000
    play_song('cotton_eye_joe.mp3')
    #start_time = pygame.time.get_ticks()
    pygame.time.set_timer(BEAT, 469)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()




        # --- updates ---



        current_time = pygame.time.get_ticks()

        #if current_time == time_check:
        #    print("time checked")
        #    time_check += 1000

        #if current_time == int(beat_time*1000):
        #    print(beat_time)
        #    rect_green.update(current_time)
        #    beat += 1
        #    beat_time = beat_times[beat]
        #    print(beat_time)


        # --- draws ---

        fenetre.fill(BLACK)
        rect_green.draw(fenetre)
        pygame.display.update()

# Downoad the song from youtube
class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
def download_mp3(url):

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])



def play_song(file_name):
    song_file = 'cotton_eye_joe.mp3'
    mp_3 = mp3.MP3(song_file)
    mixer.init(frequency=mp_3.info.sample_rate)
    mixer.music.load(song_file)
    mixer.music.play()



def libro(file_name):
    y, sr = librosa.load('cotton_eye_joe.mp3')
    hop_length = 512
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    print("libro is done")
    return beat_times



#libro('cotton_eye_joe.mp3')
#download_mp3('https://www.youtube.com/watch?v=mOYZaiDZ7BM')
#play_song('cotton_eye_joe.mp3')

main()
