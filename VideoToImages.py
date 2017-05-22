#!/usr/bin/env Python3

'''
SfMPipeline/VideoToImages.py

https://stackoverflow.com/questions/33311153/python-extracting-and-saving-video-frames
'''

__author__ = "Seyoung Park"
__copyright__ = "Copyright 2017, Seyoung Park"
__credits__ = ["Seyoung Park"]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Seyoung Park"
__email__ = "seyoung.arts.park@protonmail.com"
__status__ = "Production"


import cv2
import os

VIDEO_PATH = '/Users/young/Downloads/IMG_4188.MOV'
FRAMES_PATH_PREFIX = 'frames'

vidcap = cv2.VideoCapture(VIDEO_PATH)
success,image = vidcap.read()
count = 0
success = True


def ensure_dir():
    frames_dir = VIDEO_PATH.split('/')[-1].split('.')[0]
    frames_dir = os.path.join(FRAMES_PATH_PREFIX, frames_dir)
    if not os.path.exists(frames_dir):
        os.makedirs(frames_dir)
    return frames_dir

frames_dir = ensure_dir()

while success:
  success,image = vidcap.read()
  print 'Read a new frame: ', success
  write_path = os.path.join(frames_dir, "frame%d.jpg" % count)
  cv2.imwrite(write_path, image)     # save frame as JPEG file
  count += 1