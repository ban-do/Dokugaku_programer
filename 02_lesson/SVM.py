#SVMをつかってあやめデータを分析

#ライブラリのインポート
import sklearn.datasets as datasets
from sklearn import svm
#from sklearn import cross_validation
from sklearn.model_selection import cross_val_score

##データの取得
iris = datasets.load_iris()

#データの加工
input = iris.data[:-5]
output = iris.target[:-5]
test_input = iris.data[-5:]
test_output = iris.target[-5:]

#学習
svm = svm.SVC()
scores = cross_val_score(svm,input,output,cv=5)    #引数（アルゴリズム、入力、出力、分割サイズ）

#結果を出力
print(scores)
print("Accuracy:",scores.mean())

#評価
svm.fit(input,output)
answer = svm.predict(test_input)
print("predict anwwer:",answer)
print("Actual answer:",test_output)
