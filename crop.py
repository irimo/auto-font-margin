#coding: utf-8

import cv2
import matplotlib . pyplot as plt

def clop(path1, x, y):
    img = cv2.imread(path1, 1)
    imgwidth = img.shape[0]
    imgwidth = img.shape[1]
    width = 100
    height = 100

    trim _ img = img [ height: imgheight, width: imgwidth ]