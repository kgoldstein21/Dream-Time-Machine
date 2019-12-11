'''
This file is a test of how to get visuals to line up with the music
'''


from __future__ import unicode_literals
import numpy as np
import librosa
import os
from pygame import mixer  # Load the popular external library
from mutagen import mp3
import youtube_dl

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






download_mp3('https://www.youtube.com/watch?v=mOYZaiDZ7BM')
play_song('cotton_eye_joe.mp3')
