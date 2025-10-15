# 文件名: cnn_mnist.py
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

# 1. 加载数据
mnist = tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# 2. 数据预处理
# 归一化像素值到0-1之间
X_train, X_test = X_train / 255.0, X_test / 255.0
# 将标签转为one-hot编码（可选，取决于模型输出层的损失函数选择）
# y_train = to_categorical(y_train)
# y_test = to_categorical(y_test)
# 调整数据形状，增加一个通道维度（对于CNN是必须的）
X_train = X_train.reshape((X_train.shape[0], 28, 28, 1))
X_test = X_test.reshape((X_test.shape[0], 28, 28, 1))

# 3. 构建CNN模型
model = models.Sequential()
# 第一个卷积层：32个卷积核，大小5x5，激活函数ReLU
model.add(layers.Conv2D(32, (5, 5), activation='relu', input_shape=(28, 28, 1)))
# 第一个池化层：窗口大小2x2
model.add(layers.MaxPooling2D((2, 2)))
# 第二个卷积层：64个卷积核，大小5x5，激活函数ReLU
model.add(layers.Conv2D(64, (5, 5), activation='relu'))
# 第二个池化层
model.add(layers.MaxPooling2D((2, 2)))
# 将多维数据展平为一维，以便输入全连接层
model.add(layers.Flatten())
# 全连接层
model.add(layers.Dense(128, activation='relu'))
# 输出层，10个单元，使用softmax激活函数进行多分类
model.add(layers.Dense(10, activation='softmax'))

# 打印模型结构
model.summary()

# 4. 编译模型
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy', # 如果标签未one-hot，用此损失函数
              # loss='categorical_crossentropy', # 如果标签已one-hot，用此损失函数
              metrics=['accuracy'])

# 5. 训练模型
history = model.fit(X_train, y_train, 
                    epochs=5, 
                    validation_data=(X_test, y_test))

# 6. 评估模型
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)
print(f'\n测试准确率: {test_acc}')

# 7. 可视化训练过程
plt.plot(history.history['accuracy'], label='training accuracy')
plt.plot(history.history['val_accuracy'], label = 'testing accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.show()