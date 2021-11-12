#coding: utf-8

import cv2
import numpy as np
import math

def crop():
    law_path = "./resource/law1.jpg"
    img_origin = cv2.imread(law_path)
    img_gray = cv2.cvtColor(img_origin, cv2.COLOR_BGR2GRAY)
    # 二値化の閾値は画像を見て調整する
    ret, img_binary = cv2.threshold(img_gray, 200, 255,cv2.THRESH_BINARY)
    # ガウスぼかし
    img_blur = UnSharpMasking(img_binary, 1.0)
    # ret, img_binary = cv2.threshold(img_gray, 200, 255,cv2.THRESH_BINARY)
    # contours, hierarchy = cv2.findContours(img_blur, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    # img_contour = cv2.drawContours(img_origin, contours, -1, (0, 255, 0), 5)

    # 輪郭を１つずつ書き込んで出力
    # for i in range(len(contours)):
    #     im_con = img_origin.copy()
    #     cv2.drawContours(img_origin, contours, i, (0,255,0), 2)
    #     cv2.imwrite('./resource/work/result' + str(i) + '.png', im_con)

    img1 = img_blur
    cv2.imwrite("./resource/work/hoge.jpg", img1)

    # img = cv2.imread(path1, 1)
    # imgwidth = img.shape[0]
    # imgwidth = img.shape[1]
    # width = 100
    # height = 100

    # trim _ img = img [ height: imgheight, width: imgwidth ]

def UnSharpMasking(gray, tmp_k=3.0):
    k = math.floor(tmp_k)
    # m = math.floor(tmp_m / 2) * 2 + 1
    blur = cv2.blur(gray, (k, k))
    # kernel = np.ones((m, m))
    # i = 0
    # for range in kernel:
    #     j = 0
    #     for o in range:
    #         p:float = -1 / float(m*m)
    #         kernel[i][j] = p
    #         j += 1
    #     i += 1
    # kernel[math.floor(m/2)][math.floor(m/2)] = 1 + (8 / float(m*m))
    # _kernel = np.array([[-k/9.0, -k/9.0, -k/9.0],
    #                 [-k/9.0, 1 + (8 * k)/9.0, -k/9.0],
    #                 [-k/9.0, -k/9.0, -k/9.0]])
    # dst = cv2.filter2D(gray, -1, kernel)
    # print(kernel)
    
    return blur


crop()
