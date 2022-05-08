import os, glob
import numpy as np
import cv2
from sklearn import model_selection

X = []
Y = []

files = glob.glob("./mini/*.jpg")
for i, file in enumerate(files):
    load_image = cv2.imread(file)
    data = np.array(load_image)
    X.append(data)
    Y.append(i)
X = np.array(X)
Y = np.array(Y)
# https://stackfinder.jp.net/questions/66081001/visibledeprecationwarning-creating-an-ndarray-from-ragged-nested-sequences
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y)
xy = (X_train, X_test, y_train, y_test)
np.save("./autumn_n_judge.npy", xy)