#ロジスティック回帰を用いたあやめデータの学習

#ライブラリのimport
import sklearn.datasets as datasets
from sklearn.linear_model import LogisticRegression
#from sklearn import cross_validation
from sklearn.model_selection import cross_val_score

#データの取得
iris = datasets.load_iris()

#データの加工
input = iris.data[iris.target != 2]
output = iris.target[iris.target != 2]

#ロジスティック回帰による学習、クロスバリデーションによる評価
logi = LogisticRegression() #アルゴリズムのインスタンス生成
scores = cross_val_score(logi,input,output,cv=5)    #引数（アルゴリズム、入力、出力、分割サイズ）

#結果を出力
print(scores)
