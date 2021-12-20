import cv2
import os
import math
import numpy as np

def a_padding(top_per=10, right_per=10, bottom_per=10, left_per=10):
    glyphname = "A"
    path = "./dist/pngs/"+glyphname+".png"
    img_origin_alpya = cv2.imread(path, -1)

    a = img_origin_alpya[:, :, 3]
    ex_a = a
    y = 0
    for y_count in a:
        x = 0
        for x_count in y_count:
            ex_a[y, x] = abs(a[y, x] - 255)
            x += 1
        y += 1
    img_origin_alpya[:, :, 0] = ex_a
    img_origin_alpya[:, :, 1] = ex_a
    img_origin_alpya[:, :, 2] = ex_a
    img_origin_alpya[:, :, 3] = np.full((1, 1), 255)
    tmp_png_path = "./resource/A_origin_noalpha.png"
    cv2.imwrite(tmp_png_path, img_origin_alpya)

    img_origin = cv2.imread(tmp_png_path)
    imgheight = img_origin.shape[0]
    imgwidth = img_origin.shape[1]

    left_pos = math.floor(imgwidth * left_per / 100)
    top_pos = math.floor(imgheight * top_per / 100)

    new_width = left_pos + imgwidth + math.floor(imgwidth * right_per / 100)
    new_height = top_pos + imgheight + math.floor(imgheight * bottom_per / 100)

    new_img = cv2.resize(np.zeros((1, 1, 3), np.uint8), (new_width, new_height))
    new_img[:, :, :] = np.full((new_height, new_width,3), 255)
    new_img[top_pos:(top_pos + imgheight), left_pos:(left_pos + imgwidth)] = img_origin

    dir = "./resource/"+glyphname
    if not os.path.exists(dir):
        os.mkdir(dir)
    cv2.imwrite(dir+"/"+str(top_per)+"_"+str(right_per)+"_"+str(bottom_per)+"_"+str(left_per)+".png", new_img)

def origin_to_square():
    glyphname = "A"
    png_path = "./resource/A_origin_noalpha.png"

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

    dir = "./resource/"+glyphname
    if not os.path.exists(dir):
        os.mkdir(dir)
    cv2.imwrite(dir+"/" + glyphname + "_square.png", new_img)

def square_to_ratio(input_angle=45):
    glyphname = "A"
    square_path = "./resource/A/origin/A_square.png"
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
    dir = "./resource/"+glyphname+"/angle"
    if not os.path.exists(dir):
        os.mkdir(dir)
    dir += "/origin"
    if not os.path.exists(dir):
        os.mkdir(dir)
    cv2.imwrite(dir+"/" + str(input_angle) + ".png", img2)

def calc_arg_angle(input_angle=0):
    angle = 90 - input_angle
    return float(angle)

def various_size(input_angle=100, side_pixel=10):
    glyphname = "A"
    origin_dir = "./resource/"+glyphname+"/angle/origin"
    origin_path = origin_dir + "/" + str(input_angle) + ".png"
    img = cv2.imread(origin_path)
    new_img = cv2.resize(img, (side_pixel, side_pixel))
    dir = origin_dir + "/" + str(input_angle)
    if not os.path.exists(dir):
        os.mkdir(dir)
    cv2.imwrite(dir +"/" + str(side_pixel) +".png", new_img)
    
def various_padding_xy(input_angle=100, side_pixel=20, max_side=100, x=0, y=0):
    glyphname = "A"
    origin_dir = "./resource/" + glyphname + "/angle/origin/"+ str(input_angle)
    origin_path = origin_dir + "/" + str(side_pixel) + ".png"
    img = cv2.imread(origin_path)
    #高さを定義
    height = img.shape[0]                         
    #幅を定義
    width = img.shape[1]  

    # new_img = cv2.resize(np.zeros((1, 1, 3), np.uint8), (width, height))
    new_img = cv2.resize(np.zeros((1, 1, 3), np.uint8), (max_side, max_side))
    new_img[:, :, :] = np.full((max_side, max_side,3), 255)
    new_img[y:y+height, x:x+width] = img
    # new_img[:, :] = img
    dir = "./resource/" + glyphname + "/angle/" + str(input_angle)
    if not os.path.exists(dir):
        os.mkdir(dir)
    cv2.imwrite(dir + "/" + str(x) + "_" + str(y) + ".png", new_img)

    # dir = origin_dir + "/" + str(input_angle)
def various_padding(input_angle=100, side_pixel=20, max_side=100, increment=5):
    for x in range(0, (max_side - side_pixel), increment):
        for y in range(0, (max_side - side_pixel), increment):
            various_padding_xy(input_angle, side_pixel, max_side, x, y)
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
def various_image_output():
    increment = 20

    origin_to_square()
    for i in range(180, increment):
        square_to_ratio(input_angle=i)
    side_pixel_min = 20
    max_side = 100
    for input_angle in range(0,max_side,increment):
        for side_pixel in range(side_pixel_min,max_side,increment):
            various_size(input_angle, side_pixel)
    for input_angle in range(0, 180, increment):
        for side_pixel in range(20, 100, increment):
            various_padding(input_angle=input_angle, side_pixel=side_pixel, increment=increment)
various_image_output()
