'''
This file is a test of how to play a song using the pygame mixer
'''

import pygame, mutagen.mp3

song_file = "cotton_eye_joe.mp3"

mp3 = mutagen.mp3.MP3(song_file)
pygame.mixer.init(frequency=mp3.info.sample_rate)

pygame.mixer.music.load(song_file)
pygame.mixer.music.play()
