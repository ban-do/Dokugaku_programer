#SVMとPCAを用いてSVMの結果を可視化

#必要なライブラリのインポート
from sklearn import svm
from sklearn import datasets
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

#データの読み込み
iris = datasets.load_iris()

#PCAによってデータを二次元に変換
pca = PCA(n_components = 2)
data = pca.fit(iris.data).transform(iris.data)

#メッシュ作成
datamax = data.max(axis = 0) + 1
datamini = data.min(axis = 0) - 1
n = 200 #メッシュの細かさを指定
X,Y = np.meshgrid(np.linspace(datamini[0],datamax[0],n),
                  np.linspace(datamini[1],datamax[1],n))

#分類
svc = svm.SVC()
svc.fit(data,iris.target)
Z = svc.predict(np.c_[X.ravel(),Y.ravel()])

#描画
plt.contour(X,Y,Z.reshape(X.shape),colors = "k")
for c, s in zip([0,1,2],["o","+","x"]):
    d = data[iris.target == c]
    plt.scatter(d[:,0],d[:,1],c = "k", marker = s)

plt.show()
