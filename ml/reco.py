import numpy as np
import tensorflow as tf
import tensorflow_datasets as tfds
import os

model = tf.keras.models.load_model('./model_inc1_20oki_0-180.h5')
model.summary()

path = './A_60.npy'
img =  np.load(path, allow_pickle=True)

print(img.shape)

img = (np.expand_dims(img,0))

print(img.shape)

predictions_single = model.predict(img)

print(predictions_single)

print("予測角度(左90度を0としている): ")

predict = np.argmax(predictions_single[0])

print(predict)