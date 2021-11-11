#coding: utf-8

import cv2

def crop():
    law_path = "./resource/law1.jpg"
    im = cv2.imread(law_path)
    img_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # 二値化の閾値は画像を見て調整する
    ret, img_binary = cv2.threshold(img_gray, 200, 255,cv2.THRESH_BINARY)

    img1 = img_binary
    cv2.imwrite("./resource/work/hoge.jpg", img1)

    # img = cv2.imread(path1, 1)
    # imgwidth = img.shape[0]
    # imgwidth = img.shape[1]
    # width = 100
    # height = 100

    # trim _ img = img [ height: imgheight, width: imgwidth ]

crop()
