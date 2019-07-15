#モジュールのインストール
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model,datasets

#乱数の生成（100個のデータ、1次元、ノイズは20）
randata = datasets.make_regression(100,1,noise = 10.0)

#学習を行いモデルのパラメータを表示
lin = linear_model.LinearRegression() #線形回帰クラスのインスタンスを生成
lin.fit(randata[0],randata[1]) #フィッティング計算
print("係数:",lin.coef_)
print("切片:",lin.intercept_)
print("score:",lin.score(randata[0],randata[1]))

x = [-2.5,2.5]
plt.plot(x,lin.coef_ * x + lin.intercept_)
plt.scatter(randata[0],randata[1])

plt.show()
