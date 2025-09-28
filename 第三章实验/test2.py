# ========================================================== 
# # 西瓜书习题 3.5：Fisher LDA 完整实现（含投影方向箭头）
# ========================================================== 
import numpy as np
import pandas as pd
import io
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

#2.FisherLDA 手工实现
class FisherLDA:
    def fit(self, X, y):
        self.X0, self.X1 = X[y == 0], X[y == 1] 
        self.mu0 = self.X0.mean(axis=0) 
        self.mu1 = self.X1.mean(axis=0)

        # 类内散度矩阵 S_w
        Sw = (np.cov(self.X0, rowvar=False, ddof=1) * (self.X0.shape[0] - 1) + np.cov(self.X1, rowvar=False, ddof=1) * (self.X1.shape[0] - 1))
        # 最优投影方向
        self.w = np.linalg.inv(Sw) @ (self.mu1 - self.mu0)
        self.threshold = 0.5 * self.w @ (self.mu0 + self.mu1) 
        
        return self.w, self.threshold
    
    def predict(self, X): return (X @ self.w > self.threshold).astype(int)
    def score(self, X, y): return (self.predict(X) == y).mean()

lda = FisherLDA()
w, z_t = lda.fit(X, y) 
acc = lda.score(X, y)
print('Fisher LDA 投影方向 w=',w)
print('一维阈值 z_t =', z_t)
print('训练集准确率 =', acc)

#3. 可视化：决策边界 + 投影方向箭头
plt.figure(figsize=(6, 4))
plt.scatter(lda.X0[:, 0], lda.X0[:, 1], c='b', marker='x', label='坏瓜')
plt.scatter(lda.X1[:, 0], lda.X1[:, 1], c='r', marker='o', label='好瓜')

# 决策边界（垂直于 w）
mid = (lda.mu0 + lda.mu1) / 2
x_line = np.linspace(X[:, 0].min() - 0.05, X[:, 0].max() + 0.05, 200)
y_line = mid[1] - w[0] / w[1] * (x_line - mid[0])
plt.plot(x_line, y_line, 'g-', lw=2, label='决策边界（垂直于 w）')

# 投影方向箭头（红色）
plt.arrow(mid[0], mid[1], w[0], w[1], head_width=0.02, head_length=0.02, fc='red', ec='red', label='投影方向 w')
plt.xlim(x_line.min(), x_line.max())
plt.ylim(X[:, 1].min() - 0.05, X[:, 1].max() + 0.05)
plt.xlabel('密度')
plt.ylabel('含糖率')
plt.title('西瓜 3.0α—— Fisher LDA（习题 3.5）')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()