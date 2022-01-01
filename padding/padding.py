import cv2
import os, glob
import math
import numpy as np


origin_dir = "./dist/pngs"
noalpha_dir = "./dist/noapngs"
girigiri_dir = "./dist/giripng"
square_dir = "./dist/square"
angle_dir = "./resource/angle"

# SVG から変換すると透明になるので不透明にする。ついでに縮める
def alpha_to_noalpha(origin_path):
    glyphname = "A"
    # origin_path = origin_dir + "/A_0.png"
    img_origin = cv2.imread(origin_path, -1)
    imgheight = img_origin.shape[0]
    imgwidth = img_origin.shape[1]
    img_origin_28 = cv2.resize(img_origin, (imgwidth//10, imgheight//10))

    for y in range(img_origin_28.shape[0]):
        for x in range(img_origin_28.shape[1]):
            alpha = img_origin_28[y, x, 3]
            pixel = abs(255-alpha)
            img_origin_28[y, x, 0] = pixel
            img_origin_28[y, x, 1] = pixel
            img_origin_28[y, x, 2] = pixel
            img_origin_28[y, x, 3] = 255
    noalpha_path = noalpha_dir + "/" + glyphname + "/" + os.path.basename(origin_path)
    if not os.path.exists(noalpha_dir):
        os.mkdir(noalpha_dir)

    cv2.imwrite(noalpha_path, img_origin_28)

# パディングをギリギリなくす
def noalpha_to_girigiri(noalpha_path):
    glyphname = "A"
    # noalpha_path = noalpha_dir + "/A_0.png"

    img_origin = cv2.imread(noalpha_path)
    imgheight = img_origin.shape[0]
    imgwidth = img_origin.shape[1]
    left_x = 0
    top_y = 0
    right_x = imgwidth
    bottom_y = imgheight
    once_flag = False
    for y in range(imgheight):
        for x in range(imgwidth):
            pixel = img_origin[y, x, 0]
            if pixel < 255 & once_flag == False:
                left_x = x
                top_y = y
                once_flag = True
            right_x = x
            bottom_y = y
    girigiri_img = cv2.resize(np.zeros((1, 1, 3), np.uint8), (right_x - left_x, bottom_y - top_y))
    girigiri_img[:, :] = img_origin[top_y:bottom_y, left_x:right_x]
    girigiri_path = girigiri_dir + "/" + glyphname + "/" + os.path.basename(noalpha_path)
    if not os.path.exists(girigiri_dir):
        os.mkdir(girigiri_dir)
    
    cv2.imwrite(girigiri_path, girigiri_img)

# ギリギリ画像を正方形にする（？）
def girigiri_to_square(png_path):
    glyphname = "A"
    # png_path = "./resource/A_origin_noalpha.png"

    img_origin = cv2.imread(png_path)
    imgheight = img_origin.shape[0]
    imgwidth = img_origin.shape[1]

    new_width = max(imgwidth, imgheight)
    new_height = max(imgwidth, imgheight)
    new_img = cv2.resize(np.zeros((1, 1, 3), np.uint8), (new_width, new_height))
    new_img[:, :, :] = np.full((new_height, new_width,3), 255)

    # 縦が長い
    if (imgwidth < imgheight):
        add_padding = math.floor((imgheight - imgwidth) / 2)
        new_img[:, add_padding:(add_padding + imgwidth)] = img_origin
    else:
        add_padding = math.floor((imgwidth - imgheight) / 2)
        new_img[add_padding:(add_padding + imgheight), :] = img_origin

    if not os.path.exists(square_dir):
        os.mkdir(square_dir)
    cv2.imwrite(square_dir + "/" + glyphname + "/" + os.path.basename(png_path), new_img)

# 正方形画像から、回転をいろんな角度でさせた画像を生成する
def square_to_ratio(square_path, input_angle):
    glyphname = "A"
    # square_path = "./resource/A/origin/A_square.png"
    img = cv2.imread(square_path)
    #高さを定義
    height = img.shape[0]                         
    #幅を定義
    width = img.shape[1]  
    #回転の中心を指定                          
    center = (int(width/2), int(height/2))
    #回転角を指定
    # angle = 45.0
    angle = calc_arg_angle(input_angle)
    #スケールを指定
    scale = 1.0
    #getRotationMatrix2D関数を使用
    trans = cv2.getRotationMatrix2D(center, angle , scale)
    #アフィン変換
    img2 = cv2.warpAffine(img, trans, (width,height), borderValue=(255, 255, 255))
    if not os.path.exists(angle_dir):
        os.mkdir(angle_dir)
    dir = angle_dir + "/" + glyphname
    if not os.path.exists(dir):
        os.mkdir(dir)
    dir += "/origin"
    if not os.path.exists(dir):
        os.mkdir(dir)
    dir += "/" + str(input_angle)
    if not os.path.exists(dir):
        os.mkdir(dir)
    cv2.imwrite(dir + "/" + glyphname + "/" + os.path.basename(square_path), img2)

def calc_arg_angle(input_angle=0):
    angle = 90 - input_angle
    return float(angle)

# def various_size(input_angle=100, side_pixel=10):
#     glyphname = "A"
#     origin_dir = "./resource/"+glyphname+"/angle/origin"
#     origin_path = origin_dir + "/" + str(input_angle) + ".png"
#     img = cv2.imread(origin_path)
#     new_img = cv2.resize(img, (side_pixel, side_pixel))
#     dir = origin_dir + "/" + str(input_angle)
#     if not os.path.exists(dir):
#         os.mkdir(dir)
#     # resource/A/angle/origin/100/10.png
#     cv2.imwrite(dir +"/" + str(side_pixel) +".png", new_img)
    
# def various_padding_xy(input_angle=100, side_pixel=20, max_side=100, x=0, y=0):
#     glyphname = "A"
#     origin_dir = "./resource/" + glyphname + "/angle/origin/"+ str(input_angle)
#     origin_path = origin_dir + "/" + str(side_pixel) + ".png"
#     img = cv2.imread(origin_path)
#     #高さを定義
#     height = img.shape[0]                         
#     #幅を定義
#     width = img.shape[1]  

#     # new_img = cv2.resize(np.zeros((1, 1, 3), np.uint8), (width, height))
#     new_img = cv2.resize(np.zeros((1, 1, 3), np.uint8), (max_side, max_side))
#     new_img[:, :, :] = np.full((max_side, max_side,3), 255)
#     new_img[y:y+height, x:x+width] = img
#     # new_img[:, :] = img
#     dir = "./resource/" + glyphname + "/angle/" + str(input_angle)
#     if not os.path.exists(dir):
#         os.mkdir(dir)
#     cv2.imwrite(dir + "/" + str(x) + "_" + str(y) + ".png", new_img)

#     # dir = origin_dir + "/" + str(input_angle)
# def various_padding(input_angle=100, side_pixel=20, max_side=100, increment=5):
#     for x in range(0, (max_side - side_pixel), increment):
#         for y in range(0, (max_side - side_pixel), increment):
#             various_padding_xy(input_angle, side_pixel, max_side, x, y)
# for t in range(200): 
#     for r in range(200): 
#         for b in range(200):
#             for l in range(200):
#                 a_padding(t, r, b, l)
# def square_to_ratio_output(increment=5):
#     for i in range(180,increment):
#         square_to_ratio(i)
# def various_size_output(increment=5):
# def various_sizes_various_padding(input_angle=100, increment=5, side_pixel=20):
#     for side_pixel in range(20, 100, increment):
#         various_padding(input_angle=input_angle, side_pixel=side_pixel, max_side=100, increment=5)
# 画像を全部消すとバグる
# def various_image_output():
#     increment = 20

#     origin_to_square()
#     for i in range(180, increment):
#         square_to_ratio(input_angle=i)
#     side_pixel_min = 20
#     max_side = 100
#     for input_angle in range(0,max_side,increment):
#         for side_pixel in range(side_pixel_min,max_side,increment):
#             various_size(input_angle, side_pixel)
#     for input_angle in range(0, 180, increment):
#         for side_pixel in range(20, 100, increment):
#             various_padding(input_angle=input_angle, side_pixel=side_pixel, increment=increment)
# various_image_output()

def origin_to_square():
    files = glob.glob(origin_dir + "/*.png")
    for i, file in enumerate(files):
        alpha_to_noalpha(file)
    files = glob.glob(noalpha_dir + "/*.png")
    for i, file in enumerate(files):
        noalpha_to_girigiri(file)
    files = glob.glob(girigiri_dir + "/*.png")
    for i, file in enumerate(files):
        girigiri_to_square(file)

def square_2_ratio():
    increment = 1
    files = glob.glob(square_dir + "/*.png")
    for i, file in enumerate(files):
        # angle = 45
        for angle in range(0, 180, increment):
            square_to_ratio(square_path=file, input_angle=angle)
square_2_ratio()