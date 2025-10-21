# 文件名: cnn_mnist.py
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
import time  # 导入time模块

# 1. 加载数据
mnist = tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# 2. 数据预处理
X_train, X_test = X_train / 255.0, X_test / 255.0
X_train = X_train.reshape((X_train.shape[0], 28, 28, 1))
X_test = X_test.reshape((X_test.shape[0], 28, 28, 1))

# 3. 构建CNN模型
model = models.Sequential()
model.add(layers.Conv2D(32, (5, 5), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (5, 5), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

model.summary()

# 4. 编译模型
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 5. 训练模型
print("开始训练模型...")
start_time = time.time()  # 记录训练开始时间
history = model.fit(X_train, y_train, 
                    epochs=5, 
                    validation_data=(X_test, y_test))
end_time = time.time()  # 记录训练结束时间
print(f"训练时间: {end_time - start_time:.2f} 秒")

# 6. 评估模型
print("开始评估模型...")
start_time = time.time()  # 记录评估开始时间
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)
end_time = time.time()  # 记录评估结束时间
print(f"评估时间: {end_time - start_time:.2f} 秒")
print(f'\n测试准确率: {test_acc}')

# 7. 可视化训练过程
plt.plot(history.history['accuracy'], label='training accuracy')
plt.plot(history.history['val_accuracy'], label = 'testing accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.show()