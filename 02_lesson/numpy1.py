import numpy as np

a = np.array([[1,2],[3,4]])
print (a)

b = np.arange(10)
print(b)

c = b.reshape(2,5)
print(c)

print(a.T)

d = a+a.T
print(d)

print(np.dot(a,d))

print(a)

u = a[:,0]

print(u)

w = np.array([True,False,True,False,True,False,True,False,True,False])
print(b[w])

print (b<5)
print (b[b<5])

x = np.c_[a,a]
print(x)

y = np.r_[a,a]
print(y)
