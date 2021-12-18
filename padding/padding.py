import cv2
import os
import math
import numpy as np

def a_padding(top_per=10, left_per=10, bottom_per=10, right_per=10, ratio=0, zoom=0):
    glyphname = "A"
    path = "./dist/pngs/"+glyphname+".png"
    img_origin = cv2.imread(path, flags=cv2.IMREAD_GRAYSCALE)
    imgheight = img_origin.shape[0]
    imgwidth = img_origin.shape[1]

    left_pos = math.floor(imgwidth * left_per / 100)
    top_pos = math.floor(imgheight * top_per / 100)

    new_width = left_pos + imgwidth + math.floor(imgwidth * right_per / 100)
    new_height = top_pos + imgheight + math.floor(imgheight * bottom_per / 100)

    new_img = cv2.resize(np.zeros((1, 1, 3), np.uint8), (new_width, new_height))
    # new_img[top_pos:(top_pos + imgheight), left_pos:(left_pos + imgwidth)] = img_origin

    # new_img[:imgheight, :imgwidth] = img_origin
    dir = "./resource/"+glyphname
    if not os.path.exists(dir):
        os.mkdir(dir)
    cv2.imwrite(dir+"/"+str(top_per)+"_"+str(left_per)+"_"+str(bottom_per)+"_"+str(right_per)+"_"+str(ratio)+"_"+str(zoom)+".png", img_origin)

a_padding()