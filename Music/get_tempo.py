'''
This file takes in an mp3 file and processes it to find the tempo of the song
'''


from __future__ import print_function
import librosa

# 1. Get the file path to the included audio example
filename = librosa.util.example_audio_file()

# loads the audio as a waveform `y`
#  stores the sampling rate as `sr`
y, sr = librosa.load(filename)

# runs the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

#print the tempo
print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

# convert the frame indices of beat events into timestamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)
