import numpy as np
from scipy import sparse

a = sparse.lil_matrix((5,5))
print(a)
a[0,0] = 1;a[1,1] = 1;a[2,2] = 1;a[3,3] = 1;a[4,4] = 1
print(a)
v = np.array([1,2,3,4,5])
print(a.dot(v))

b = a.tocsr()
print(b)
print(b.getrow(0))
