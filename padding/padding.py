import cv2
import os
import math
import numpy as np

def a_padding(top_per=10, left_per=10, bottom_per=10, right_per=10, ratio=0, zoom=0):
    glyphname = "A"
    path = "./dist/pngs/"+glyphname+".png"
    img_origin = cv2.imread(path, -1)
    imgheight = img_origin.shape[0]
    imgwidth = img_origin.shape[1]

    a = img_origin[:, :, 3]
    ex_a = a
    y = 0
    for y_count in a:
        x = 0
        for x_count in y_count:
            ex_a[y, x] = abs(a[y, x] - 255)
            x += 1
        y += 1
    img_origin[:, :, 0] = ex_a
    img_origin[:, :, 1] = ex_a
    img_origin[:, :, 2] = ex_a
    img_origin[:, :, 3] = np.full((1, 1), 255)

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