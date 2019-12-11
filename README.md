# Dream Time Machine

### Dream Time Machine is an audio-enhanced visual experience that combines video altered with Google's Deep Dream with an interactive live videocam feed.

## Table of Contents
- [Introduction](#Introduction "Introduction")
- [Getting Started](#Getting-Started "Getting Started")  
- [Deployment](#Deployment "Deployment")
- [System Architecture](#System-Architecture "System Architecture")
- [Feedback](#Feedback "Feedback")
- [Team](#Team "Team")  

## Introduction
This repository contains code to run an "audio-visual experience" in python in which the user's outline is superimposed on top of a trippy video that we created. The video detects you face and pulses shapes out from it to the beat of the song it plays. Songs and modes of the video can be chosen before the video starts. Read on to learn how to start your very own deep dream experience.

<img src="https://raw.githubusercontent.com/kgoldstein21/Dream-Time-Machine/master/DreamImages/team_dream_5xZoom_3a3x3.jpeg" alt="team dream" width="500"/>


In brief, Google Deep Dream is a computer vision program that deliberately over-processes images. It works by taking in a neural network that’s already been trained on a certain set of images, then telling that neural network to recognize patterns in whatever the input image is. It repeats this several times to create truly unsettling images.


## Getting Started
### Deep Dream
You will have to install Caffe and Google Protobuf to get Google Deep Dream up and running:

  `conda install -c anaconda protobuf`

  `conda install -c anaconda caffe`

(For these to work, you might have to install the Caffe and Protobuf files separately for Anaconda to install the Python wrapper for them)

`sudo apt install caffe-cpu`

### OpenCV
This project also makes use of image processing and computer vision library OpenCV. To get this library installed, run the following pip install:

`$ pip install opencv-python`

### Audio Processing

In order to download your own songs and change the audio processing if you wish, there are a few packages you need to download. Run the following commands to download those packages:

`$ pip install Pillow`
`$ pip install librosa`
`$ pip install mutagen`

### Interface

To get the interface up and running, install pygame in the command using the following prompt:

`$ pip install pygame`


## Deployment

To run the program, just download the repository, and open up ##FILENAME-HERE. Then sit back, get up, dance around, do whatever you feel as the program creates an entertaining visual addition to the tunes.

## System Architecture

Our program relies heavily on pre-loaded media. We have many different programs that all work to create this preloaded media. The background video is made of images that are processed using Google's deep dream algorithm in a jupyter notebook. The songs are downloaded from youtube as mp3's and then their data is extracted using librosa.

The live portion of our program combines all these preloaded parts as well as a couple other compnonents. The experience starts with a launch screen where you choose your settings. Once the actual experience starts, the program plays the song, displays the deep-dreamed images as a video, and uses openCV to overlay an outline of the camera feed, detect faces, and create shapes to the beat of the song.

![Image of System Architecture Diagram](https://github.com/kgoldstein21/Dream-Time-Machine/blob/master/finalprojectsystemarch.JPG "system architecture diagram")



## Feedback
If you have any questions about this project or would like to contribute in some way, feel free to [email us](mailto:ator@olin.edu "ator@olin.edu")!

## Team
Afraz Padamsee [@apadamsee](https://github.com/apadamsee "Afraz's GitHub")

Annie Tor [@ator1](https://github.com/ator1 "Annie's GitHub")   

Christian Quijano [@Cuijor](https://github.com/Cuijor "Christian's Github")

Katie Goldstein [@kgoldstein21](https://github.com/kgoldstein21 "Katie's GitHub")
