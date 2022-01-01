#coding: utf-8

import cv2
import numpy as np
import math
import copy
import os

def crop(law_path = "./resource/law1.jpg"):
    # law_path = "./resource/law1.jpg"
    img_origin = cv2.imread(law_path)
    imgheight = img_origin.shape[0]
    imgwidth = img_origin.shape[1]
    ratio = 7
    padding = 20
    ret, img_binary = cv2.threshold(img_origin, 200, 255,cv2.THRESH_BINARY)
    img_gray_highlight = cv2.cvtColor(img_binary, cv2.COLOR_BGR2GRAY)
    # 縮小
    resize_w = math.floor(imgwidth / ratio)
    resize_h = math.floor(imgheight / ratio)
    img_mini = cv2.resize(img_gray_highlight, (resize_w, resize_h))
    # ガウスぼかし
    img_blur = UnSharpMasking(img_mini, 5.0)
    # 二値化で少しでもグレーなところを黒くする
    r, img_binary_mini = cv2.threshold(img_blur, 254, 255, cv2.THRESH_BINARY)
    img_gray_color_mini = cv2.cvtColor(img_binary_mini, cv2.COLOR_GRAY2BGR)
    # 輪郭検出
    contours, img_rinkaku_mini = cv2.findContours(img_binary_mini, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # img_contour = cv2.drawContours(img_gray_color_mini, contours, -1, (0, 255, 0), 2)
    i = 0
    for point in contours:
        img_gray_color_mini_work = copy.copy(img_gray_color_mini)
        x, y, w, h = cv2.boundingRect(point)
        crop_x = max(x * ratio - padding, 0)
        crop_y = max(y * ratio - padding, 0)
        crop_w = min(w * ratio + padding * 2, resize_w)
        crop_h = min(h * ratio + padding * 2, resize_h)
        # if (i == 31):
        #     print(x, y, w, h, sep=' ')
        #     print(crop_x, crop_y, crop_w, crop_h, sep=' ')
        # cv2.rectangle(img_gray_color_mini_work, (x, y), (x + w, y + h), (0, 255, 0), -1)
        cv2.fillConvexPoly(img_gray_color_mini_work, points =point, color=(0, 255, 0))
        # crop_image_mini = img_mini[crop_y:crop_y+crop_h, crop_x:crop_x+crop_w]
        crop_image = img_gray_highlight[crop_y:crop_y+crop_h, crop_x:crop_x+crop_w]
        # crop_image = img_gray_color_mini_work[y:y+h,x:x+w]
        cv2.imwrite("./resource/work/" + str(os.path.basename(law_path)).split('.')[0] + "-" + str(i)+".jpg", crop_image)
        # cv2.imshow("Cropped", crop_image)
        i += 1
    
    # 輪郭を１つずつ書き込んで出力
    # for i in range(len(contours)):
    #     im_con = img_origin.copy()
    #     cv2.drawContours(img_origin, contours, i, (0,255,0), 2)
    #     cv2.imwrite('./resource/work/result' + str(i) + '.png', im_con)

    # img1 = img_gray_color_mini
    # cv2.imwrite("./resource/work/hoge.jpg", img1)

    # img = cv2.imread(path1, 1)
    # imgwidth = img.shape[0]
    # imgwidth = img.shape[1]
    # width = 100
    # height = 100

    # trim _ img = img [ height: imgheight, width: imgwidth ]

def UnSharpMasking(gray, tmp_k=3.0):
    k = math.floor(tmp_k)
    blur = cv2.blur(gray, (k, k))
    return blur

crop("./resource/law1.jpg")
crop("./resource/law2.jpg")
