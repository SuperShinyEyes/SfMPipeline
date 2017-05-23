#!/usr/bin/env Python3

'''
SfMPipeline/blurriness.py

'''

__author__ = "Seyoung Park"
__copyright__ = "Copyright 2017, Seyoung Park"
__credits__ = ["Seyoung Park"]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Seyoung Park"
__email__ = "seyoung.arts.park@protonmail.com"
__status__ = "Production"

#http://www.pyimagesearch.com/2015/09/07/blur-detection-with-opencv/

import cv2

def blurriness_from_path(path):

    image = cv2.imread(imagePath)
    return blurriness(image)

def blurriness(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.Laplacian(gray, cv2.CV_64F).var()
