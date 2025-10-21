# 文件名: svm_mnist.py
import time  # 添加计时模块
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

# 记录总运行时间
start_time = time.time()

# 1. 加载数据
print("正在加载MNIST数据集...")
data_start = time.time()  # 记录加载数据的开始时间
mnist = fetch_openml('mnist_784', version=1, as_frame=False, parser='auto')
X, y = mnist.data.astype('float32'), mnist.target.astype(int)
print(f"数据形状: X={X.shape}, y={y.shape}")
print(f"加载数据耗时: {time.time() - data_start:.2f} 秒")

# 2. 数据预处理
print("正在进行数据预处理...")
preprocess_start = time.time()  # 记录数据预处理的开始时间
# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
# 标准化数据（SVM对数据尺度敏感）
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print(f"数据预处理耗时: {time.time() - preprocess_start:.2f} 秒")

# 3. 训练SVM模型
print("开始训练SVM模型...")
train_start = time.time()  # 记录模型训练的开始时间
# 使用RBF核，C和gamma是重要参数[0.1, 1, 10等可调])
svm_model = SVC(kernel='rbf', C=10, gamma='scale')
svm_model.fit(X_train_scaled, y_train)
print(f"模型训练完成！耗时: {time.time() - train_start:.2f} 秒")

# 4. 模型评估
print("正在评估模型...")
eval_start = time.time()  # 记录模型评估的开始时间
y_pred = svm_model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f"\n测试集准确率: {accuracy:.4f}")
print("\n分类报告:")
print(classification_report(y_test, y_pred))
print(f"模型评估耗时: {time.time() - eval_start:.2f} 秒")

# 5. 可视化部分预测结果
print("正在可视化预测结果...")
visual_start = time.time()  # 记录可视化的开始时间
fig, axes = plt.subplots(2, 5, figsize=(12, 5))
for i, ax in enumerate(axes.flat):
    ax.imshow(X_test[i].reshape(28, 28), cmap='gray')
    ax.set_title(f"True: {y_test[i]}, Pred: {y_pred[i]}")
    ax.axis('off')
plt.tight_layout()
plt.show()
print(f"可视化耗时: {time.time() - visual_start:.2f} 秒")

# 打印总运行时间
print(f"\n总运行时间: {time.time() - start_time:.2f} 秒")