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
This project takes two inputs: a music file and a webcam video feed and outputs an interactive music video. In particular, it detects outlines from the video feed, detects faces, and then creates pulsing shapes that emanate from the center of each face that it detects. the shapes will pulse to the beats per minute of the inputted song. Additionally, the outlines will be superimposed on a video altered with Google's Deep Dream algorithm. If you're not familiar with Deep Dream, here are some examples of images created using it:

<img src="https://i.pinimg.com/originals/20/f6/82/20f6821fc2676529835c5064a3f7300b.jpg" alt="deep dream dog" width="500"/>

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

## Deployment

## System Architecture


![Image of System Architecture Diagram](https://github.com/kgoldstein21/Dream-Time-Machine/blob/master/systemarch1.jpg)

Our program has two parts, one that pre-renders and one that is updated in real-time. The pre-rendered section creates the background video. It downloads Youtube videos and runs the Google Deep Dream algorithm on
them to make a really trippy background. The real-time part has two parts in it. In the first part, the user chooses a song to play, and the program downloads the song and analyzes it as it plays. In the second part, the program takes in live video of the people using it, detects their face, and creates shapes that come out of their forehead. We're experimenting with ways that the program can be more interactive for the user. 
## Feedback
If you have any questions about this project or would like to contribute in some way, feel free to [email us](mailto:ator@olin.edu "ator@olin.edu")!

## Team
Afraz Padamsee [@apadamsee](https://github.com/apadamsee "Afraz's GitHub")

Annie Tor [@ator1](https://github.com/ator1 "Annie's GitHub")   

Christian Quijano

Katie Goldstein [@kgoldstein21](https://github.com/kgoldstein21 "Katie's GitHub")
