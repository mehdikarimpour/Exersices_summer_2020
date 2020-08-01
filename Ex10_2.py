import numpy as np
import matplotlib.pyplot as plt
vec1=np.array([-1.,4.,-9.])
mat1=np.array([[1.,3.,5.],[7.,-9.,2.],[4.,6.,8.]])
vec2=(np.pi/4)*vec1
vec2=np.cos(vec2)
vec3=vec1+2*vec2
vec4=mat1*vec3
mat1_transpose=mat1.transpose()
print(mat1_transpose)
print(np.linalg.det(mat1_transpose))
print(np.min(vec1))
print(np.amin(mat1_transpose))
A=np.array([[17, 24, 1, 8, 15],
[23, 5, 7, 14, 16],
[ 4, 6, 13, 20, 22],
[10, 12, 19, 21, 3],
[11, 18, 25, 2, 9]])
print(np.sum(A,axis=0))
print(np.sum(A,axis=1))
print(np.sum(np.diag(A)))
print(np.sum(np.fliplr(A))/5)
print("So its magical cube")
M=np.random.rand(10,10)
print(M)
print('First')
print(M[1:5,1:5])
print('second')
print(M[1:5,5:10])
print('third')
print(M[5:10,1:5])
print('last')
print(M[5:10,5:10])



