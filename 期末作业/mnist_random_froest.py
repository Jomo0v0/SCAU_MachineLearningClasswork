# 文件名: random_forest_mnist.py
import time  # 添加计时模块
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np
import matplotlib.pyplot as plt

# 1. 加载数据
start_time = time.time()
mnist = fetch_openml('mnist_784', version=1, as_frame=False, parser='auto')
X, y = mnist.data, mnist.target.astype(int)
print(f"数据加载完成，用时: {time.time() - start_time:.2f} 秒")

# 2. 数据预处理（随机森林对数据尺度不敏感，通常无需标准化）
start_time = time.time()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(f"数据预处理完成，用时: {time.time() - start_time:.2f} 秒")

# 3. 训练随机森林模型
print("开始训练随机森林模型...")
start_time = time.time()
rf_clf = RandomForestClassifier(n_estimators=100, random_state=42)
rf_clf.fit(X_train, y_train)
print(f"模型训练完成！用时: {time.time() - start_time:.2f} 秒")

# 4. 模型评估
start_time = time.time()
y_pred = rf_clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\n测试集准确率: {accuracy:.4f}")
print("\n分类报告:")
print(classification_report(y_test, y_pred))
print(f"模型评估完成，用时: {time.time() - start_time:.2f} 秒")

#（可选）查看特征重要性
start_time = time.time()
importance = rf_clf.feature_importances_
plt.bar(range(len(importance)), importance)
plt.title("Feature Importance (Random Forest)")
plt.show()
print(f"特征重要性可视化完成，用时: {time.time() - start_time:.2f} 秒")

# 5. 可视化部分预测结果
start_time = time.time()
def plot_digits(images, labels, predictions, n_col=5):
    n_images = len(images)
    n_row = n_images // n_col + (n_images % n_col != 0)
    plt.figure(figsize=(n_col*2, n_row*2))
    for i in range(n_images):
        plt.subplot(n_row, n_col, i+1)
        plt.imshow(images[i].reshape(28,28), cmap='gray', interpolation='none')
        plt.title(f"True: {labels[i]}\nPred: {predictions[i]}")
        plt.axis('off')
    plt.tight_layout()
    plt.show()

# 随机选择10个样本展示
sample_indices = np.random.choice(len(X_test), 10)
plot_digits(X_test[sample_indices], y_test[sample_indices], y_pred[sample_indices])
print(f"预测结果可视化完成，用时: {time.time() - start_time:.2f} 秒")