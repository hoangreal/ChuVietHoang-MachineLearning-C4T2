import numpy as np

#
# C = np.array([
#     [0,0],
#     [0,0],
# ])
# a = A.shape  a[1] = 3, a[0] = 2
# b = B.shape  b[0] = a[1], b[1] = 2
# c = C.shape  c[0] = a[0], c[1] = b[1]
def Matrix_Multiplication(A,B):
    r1 = A.shape[0]
    c1 = A.shape[1]
    r2 = B.shape[0]
    c2 = B.shape[1]
    if(c1 == r2):
        result = np.array([[0 for j in range(c2)] for i in range(r1)])
        for k in range(c2):
            for i in range(r1):
                for j in range(r2):
                   result[i][k] += A[i][j]*B[j][k]
        return result

# r1 = int(input())
# c1 = int(input())
# r2 = int(input())
# c2 = int(input())
C = np.array([
    [1,0,1],
    [0,1,-1],
    [3,4,5]

])
D = np.array([
    [1,0,1,2,3],
    [0,1,4,5,6],
    [1,-1,5,6,7]
])
print(Matrix_Multiplication(C,D))

#Phương pháp: Lấy từng hàng của MatA nhân với từng cột của MatB

