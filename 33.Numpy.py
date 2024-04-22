import numpy as np
array1=np.array([[1,2,3,4,5],[2,1,3,4,5]])
print(array1)
print(array1.shape)
print(np.zeros(4))
print(np.zeros((4,6)))
print(np.ones(1).dtype)
print(np.empty((4,6)))
print(array1/array1)


array2=np.array([[1,2,3],
                 [4,5,6]])
print(array2.sum(axis=1))
print(array2.sum(axis=0))