import matplotlib.pyplot as plt
import numpy as np

#直線の描画
#x = [1,2,3]
#y = [4,5,6]
#plt.plot(x,y)
#plt.show()

#二次関数の描画
#a = np.linspace(-5,5,100)
#b = a**2
#plt.plot(a,b)
#plt.show()

#散布図の描画
#c = [1,2,3,4]
#d1 = [4,3,2,1]
#d2 = [1,2,3,4]
#plt.scatter(c,d1,c ="r",marker = "o")
#plt.scatter(c,d2,c = "y",marker = "+")
#plt.show()

#等高線
x = np.linspace(-5,5,200)
y = np.linspace(-5,5,200)
X,Y = np.meshgrid(x,y)
Z = X.ravel()**2 - Y.ravel()**2
print(Z)
#contour(X軸,Y軸,値)
plt.contour(X,Y,Z.reshape(X.shape))
plt.show()
