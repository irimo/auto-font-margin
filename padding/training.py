from PIL import Image
import os, glob
import numpy as np
import cv2
from sklearn import model_selection
import pandas as pd

increment = 20

classes = range(0,180,increment)
num_classes = len(classes)
image_size = 100

'''
XとYはそれぞれ、画像データと、その画像の角度がどれなのかを示すラベル。
'''
X = []
Y = []

def training_a_ratio(ratio=100):
    glyphname = "A"
    ret_X = []
    ret_Y = []
    # for index, input_angle in enumerate(classes):
        # photos_dir = "./" + classlabel
        # for input_angle in range(0, 180, increment):
    photos_dir = "./resource/" + glyphname + "/angle/" + str(ratio)
    files = glob.glob(photos_dir + "/*.png")
    for i, file in enumerate(files):
        # if i >= 141: break # monkey,boar,crowそれぞれのデータ数の最小に合わせる
        load_image = cv2.imread(file)

        image = cv2.resize(load_image, (image_size, image_size))
        h = image.shape[0]
        w = image.shape[1]
        arr2 = image[:, :, 0]
        for y in range(h):
            for x in range(w):
                arr2[y, x] = float(image[y, x, 0] / 255)
        data = np.array(arr2)
        ret_X.append(data)
        ret_Y.append(ratio)
    # print(ret_X)
    return ret_X, ret_Y
# def image_flatten(image=[]):
#     arr1 = image[:, :, 0] # gray
#     arr2 = []
#     for y in image.shape(0):
#         for x in image.shape(1):
#             arr2[y, x] = arr1[y, x] / 255
#     arr3 = np.ndarray.flatten(arr2)
#     return np.array(arr3)
for ratio in range(0, 180, increment):
    tmp_X, tmp_Y = training_a_ratio(ratio=ratio)
    X += tmp_X
    Y += tmp_Y
print(len(X))
X = np.array(X)
Y = np.array(Y)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y)
xy = (X_train, X_test, y_train, y_test)
np.save("./dist/training_test.npy", xy)