#!/usr/bin/env Python2

'''
SfMPipeline/VideoToImagesWithFilter.py

'''

__author__ = "Seyoung Park"
__copyright__ = "Copyright 2017, Seyoung Park"
__credits__ = ["Seyoung Park"]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Seyoung Park"
__email__ = "seyoung.arts.park@protonmail.com"
__status__ = "Production"


#http://stackoverflow.com/questions/33311153/python-extracting-and-saving-video-frames

'''video2 uses a different strategy. dont know if this one is any good yet'''

import cv2
from blurriness import blurriness
import os

VIDEO_PATH = '/Users/young/Downloads/IMG_4190.MOV'
VIDEO_NAME = VIDEO_PATH.split('/')[-1].split('.')[0]
FRAMES_PATH_PREFIX = 'frames'

def video_exists():
    return os.path.exists(VIDEO_PATH)


def ensure_dir():
    frames_dir = os.path.join(FRAMES_PATH_PREFIX, VIDEO_NAME)
    if not os.path.exists(frames_dir):
        os.makedirs(frames_dir)
    return frames_dir



def main():
    if not video_exists():
        raise IOError

    frames_dir = ensure_dir()

    vidcap = cv2.VideoCapture(VIDEO_PATH)

    success,image = vidcap.read()

    window = 16
    count = 0
    success = True

    while success:

        #print("Window")
        blurs = []
        images = []

        for i in range(window):

            success, image = vidcap.read()
            if not success: break
            blur = blurriness(image)
            blurs.append(blur)
            images.append(image)
            #print "\t",i,"\tFrame",count," - Sharpness",blur
            count+=1

        winner_index = blurs.index(max(blurs))
        winner_frame = images[winner_index]
        winner_frame_count = count - window + winner_index

        #print "Saved frame",winner_frame_count,"Sharpness",blurs[winner_index]
        new_name = "{folder}/" + VIDEO_NAME + "_{num:06d}.jpg"
        #cv2.imwrite("{folder}/frame_{num:06d}.jpg".format(folder=sys.argv[2],num=winner_frame_count), images[winner_index])
        cv2.imwrite(new_name.format(folder=frames_dir,num=winner_frame_count), images[winner_index])

if __name__ == '__main__' :

    try:
        main()
    except KeyboardInterrupt as e:
        print(e, "Bye!")
    except IOError as e:
        print(e, "Wrong path", VIDEO_PATH)