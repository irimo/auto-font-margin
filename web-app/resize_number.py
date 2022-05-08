#coding: utf-8

import cv2
import numpy as np
import math
import copy
import os
import random

def crop(law_path):
    img_origin = cv2.imread(law_path)
    imgheight = img_origin.shape[0]
    imgwidth = img_origin.shape[1]
    reisze_goal = 32
    padding = 20
    ret, img_binary = cv2.threshold(img_origin, 200, 255,cv2.THRESH_BINARY)
    img_gray_highlight = cv2.cvtColor(img_binary, cv2.COLOR_BGR2GRAY)
    # 縮小
    # resize_w = math.floor(imgwidth / ratio)
    # resize_h = math.floor(imgheight / ratio)
    resize_w = 28
    resize_h = 28
    img_mini = cv2.resize(img_gray_highlight, (resize_w, resize_h))
    pos = str(math.floor(random.uniform(10000, 20000)))

    cv2.imwrite("./resource/numbers-autumn/mini/" + str(os.path.basename(law_path)).split('.')[0] + "-" + pos +".jpg", img_mini)

for i in range(0,9):
    crop("./resource/numbers-autumn/"+str(i)+".jpg")

