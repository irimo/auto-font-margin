import cv2
import math
import numpy as np

size = 28

path = "./resource/test/A_origin.png"

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

    return new_img

# 正方形画像から、回転をいろんな角度でさせた画像を生成する
def square_to_ratio(img, input_angle):
    glyphname = "A"
    # square_path = "./resource/A/origin/A_square.png"
    # img = cv2.imread(square_path)
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
    # if not os.path.exists(angle_dir):
    #     os.mkdir(angle_dir)
    # dir = angle_dir + "/" + glyphname
    # if not os.path.exists(dir):
    #     os.mkdir(dir)
    # dir += "/origin"
    # if not os.path.exists(dir):
    #     os.mkdir(dir)
    # dir += "/" + str(input_angle)
    # if not os.path.exists(dir):
    #     os.mkdir(dir)
    # cv2.imwrite(dir+"/" + os.path.basename(square_path), img2)
    return img2

def calc_arg_angle(input_angle=0):
    angle = 90 - input_angle
    return float(angle)

load_image = girigiri_to_square(path)
# ratio_image = square_to_ratio(load_image, 30)
image = cv2.resize(load_image, (size, size))
# h = image.shape[0]
# w = image.shape[1]
arr2 = image[:, :, 0]
for y in range(size):
    for x in range(size):
        arr2[y, x] = float(image[y, x, 0] / 255)
data = np.array(arr2)
np.save("./dist/autumn_A.npy", data)