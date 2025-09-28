import numpy as np
import pandas as pd
import io # 补上这一行
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis 
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Microsoft YaHei' 
plt.rcParams['axes.unicode_minus'] = False
# 加载西瓜数据集 3.0α
data = """密度 含糖率 好瓜
0.697 0.460 1
0.774 0.376 1
0.634 0.264 1
0.608 0.318 1
0.556 0.215 1
0.403 0.237 1
0.481 0.149 1
0.437 0.211 1
0.666 0.091 0
0.243 0.267 0
0.245 0.057 0
0.343 0.099 0
0.639 0.161 0
0.657 0.198 0
0.360 0.370 0
0.593 0.042 0
0.719 0.103 0"""
df = pd.read_csv(io.StringIO(data), sep=r'\s+')
X = df[['密度', '含糖率']].values
y=df['好瓜'].values


# 手动实现对率回归
class LogisticRegressionManual:
    def __init__(self, learning_rate=0.1, max_iter=50000, tol=1e-5):
        self.lr = learning_rate
        self.max_iter = max_iter
        self.tol = tol
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def fit(self, X, y):
    # 添加偏置项
        X_b = np.column_stack([np.ones(len(X)), X]) 
        self.beta = np.zeros(X_b.shape[1])

        for i in range(self.max_iter):
            h = self.sigmoid(X_b @ self.beta)
            grad = X_b.T @ (y - h)
            beta_new = self.beta + self.lr * grad
            # 检查收敛条件
            if np.linalg.norm(beta_new - self.beta) < self.tol: break
            self.beta = beta_new
        return i+1

    def predict_proba(self, X):
        X_b = np.column_stack([np.ones(len(X)), X]) 
        return self.sigmoid(X_b @ self.beta)
    
    def predict(self, X):
        return (self.predict_proba(X) > 0.5).astype(int)

# 训练对率回归模型
lr_model = LogisticRegressionManual()
iterations = lr_model.fit(X, y)
y_pred_lr = lr_model.predict(X)
acc_lr = accuracy_score(y, y_pred_lr)
print(f"对率回归迭代次数: {iterations}")
print(f"对率回归系数: {lr_model.beta}")
print(f"对率回归准确率: {acc_lr:.1%}")
# 绘制决策边界
plt.figure(figsize=(6, 5))
pos, neg = y == 1, y == 0
plt.scatter(X[pos, 0], X[pos, 1], c='r', marker='o', label='好瓜')
plt.scatter(X[neg, 0], X[neg, 1], c='b', marker='x', label='坏瓜')
x_min, x_max = X[:, 0].min() - 0.05, X[:, 0].max() + 0.05
x_line = np.linspace(x_min, x_max, 200) #beta0+beta1*x+beta2*y=0=>y=-(beta0+beta1*x)/beta2
y_line = -(lr_model.beta[0] + lr_model.beta[1] * x_line) / lr_model.beta[2]
plt.plot(x_line, y_line, 'g-', lw=2, label='对率回归边界')
plt.xlim(x_min, x_max)
plt.xlabel('密度')
plt.ylabel('含糖率')
plt.title('西瓜 3.0α —— 对率回归')
plt.legend()
plt.grid(alpha=0.3)
plt.show()