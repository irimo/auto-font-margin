import numpy as np
import tensorflow as tf
import tensorflow_datasets as tfds
import os

image_size = 50

# DATA_URL = os.path.abspath()
# path = tf.keras.utils.get_file('mnist.npz', DATA_URL)
path = './ml/training_test.npy'
data =  np.load(path, allow_pickle=True)
# train_examples = data['x_train']
# test_examples = data['x_test']
# train_labels = data['y_train']
# test_labels = data['y_test']
train_examples = data[0]
test_examples = data[1]
train_labels = data[2]
test_labels = data[3]
# print(train_labels.shape)
train_dataset = tf.data.Dataset.from_tensor_slices((train_examples, train_labels))
test_dataset = tf.data.Dataset.from_tensor_slices((test_examples, test_labels))
# print(train_examples.shape)
# データセットのシャッフルとバッチ化
BATCH_SIZE = 32
SHUFFLE_BUFFER_SIZE = 100

train_dataset = train_dataset.shuffle(SHUFFLE_BUFFER_SIZE).batch(BATCH_SIZE)
test_dataset = test_dataset.batch(BATCH_SIZE)
# with strategy.scope() 以下に入れる
# trainset = strategy.experimental_distribute_dataset(trainset)
# valset = strategy.experimental_distribute_dataset(valset)

# モデルの構築と訓練
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(image_size, image_size), name='flatten_layer'),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
#モデルのコンパイル
model.compile(optimizer=tf.optimizers.Adam(), 
              loss='mean_squared_error', # サンプルのやつえらった
              metrics=['accuracy'])
# model.compile(optimizer=tf.keras.optimizers.RMSprop(),
#                 loss=tf.keras.losses.SparseCategoricalCrossentropy(),
#                 metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])

# model.fit(train_examples, train_labels, validation_data=(test_examples, test_labels), epochs=5, steps_per_epoch=BATCH_SIZE)
model.fit(train_dataset, epochs=5, steps_per_epoch=BATCH_SIZE)
model.save("model_cnn.h5")

# test_loss, test_acc = model.evaluate(test_examples, test_labels, verbose=2)
results = model.evaluate(test_examples, test_labels, verbose=2)
print("test loss, test acc:", results)

# Generate predictions (probabilities -- the output of the last layer)
# on new data using `predict`
print("Generate predictions for 3 samples")
predictions = model.predict(test_examples[:3])
print("predictions shape:", predictions.shape)
for i in range(predictions):
    print("correct: " + test_labels[i])
    print("show: " + np.amax(predictions[i]))