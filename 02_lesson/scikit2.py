#糖尿病データを用いた線形回帰、予測

#ライブラリをimport
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets

#データの読み込み
data = datasets.load_diabetes()

#データを訓練用と評価用に分ける
train_input = data.data[:-20]    #入力データの最後の20個以外を訓練用入力データにする
train_output = data.target[:-20] #出力データの最後の20個以外を訓練用出力データにする
test_input = data.data[-20:]     #入力データの最後の20個を評価用入力データにする
test_output = data.target[-20:]  #出力データの最後の20個を評価用出力データにする

#学習を行う
lin = linear_model.LinearRegression() #線形回帰クラスのインスタンスを生成
lin.fit(train_input,train_output) #フィッティング計算

#当てはまり具合結果を表示
print("score:",lin.score(train_input,train_output))

#学習結果を用いて評価用データの１番目の入力データから予測し結果を表示
print("Prediction data:",lin.predict(test_input)[0])

#実際の値を表示
print("Actual data:",test_output[0])
