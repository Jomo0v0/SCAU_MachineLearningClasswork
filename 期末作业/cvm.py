# 文件名: svm_mnist.py
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

# 1. 加载数据
print("正在加载MNIST数据集...")
mnist = fetch_openml('mnist_784', version=1, as_frame=False, parser='auto')
X, y = mnist.data.astype('float32'), mnist.target.astype(int)
print(f"数据形状: X={X.shape}, y={y.shape}")

# 2. 数据预处理
# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
# 标准化数据（SVM对数据尺度敏感）
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. 训练SVM模型
print("开始训练SVM模型...")
# 使用RBF核，C和gamma是重要参数[0.1, 1, 10等可调])
svm_model = SVC(kernel='rbf', C=10, gamma='scale')
svm_model.fit(X_train_scaled, y_train)
print("模型训练完成！")

# 4. 模型评估
y_pred = svm_model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f"\n测试集准确率: {accuracy:.4f}")
print("\n分类报告:")
print(classification_report(y_test, y_pred))

# 5. 可视化部分预测结果
fig, axes = plt.subplots(2, 5, figsize=(12, 5))
for i, ax in enumerate(axes.flat):
    ax.imshow(X_test[i].reshape(28, 28), cmap='gray')
    ax.set_title(f"True: {y_test[i]}, Pred: {y_pred[i]}")
    ax.axis('off')
plt.tight_layout()
plt.show()
