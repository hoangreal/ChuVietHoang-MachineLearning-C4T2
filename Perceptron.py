import numpy as np
import matplotlib.pyplot as plt
import random
# def Matrix_Multiplication(A,B):
#     r1 = A.shape[0]
#     c1 = A.shape[1]
#     r2 = B.shape[0]
#     c2 = B.shape[1]
#     if(c1 == r2):
#         result = np.array([[0 for j in range(c2)] for i in range(r1)])
#         for k in range(c2):
#             for i in range(r1):
#                 for j in range(r2): #r2 == c1
#                    result[i][k] += A[i][j]*B[j][k]
#         return result
def Matrix_Multiplication(A,B):
    r1 = A.shape[0]
    c1 = A.shape[1]
    r2 = B.shape[0]
    c2 = B.shape[1]
    if(c1 == r2):
        result = np.array([[0 for j in range(c2)] for i in range(r1)])
        for k in range(c2):
            for i in range(r1):
                for j in range(r2): #r2 == c1
                   result[i][k] += A[i][j]*B[j][k]
        return result
def hardLim(a):
    if a > 0:
        a = 1
    if a <= 0:
        a = 0
    return a

count = 0
x1 = np.random.randint(0,50,size=50)
y1 = np.random.randint(0,50,size=50)
P1 = np.array([(x1[i] for i in range(50),y1[i] for i in range(50)])
t1 = []
for i in range(50):
    t1.append(0)

x2 = np.random.randint(50,100,size=50)
y2 = np.random.randint(50,100,size=50)
P2 = []
t2 = []
for i in range(50):
    P2.append((x1[i],y1[i]))
    t2.append(1)

plt.scatter(x1,y1,color= 'r')
plt.scatter(x2,y2,color= 'g')

plt.xlim(0,100)
plt.ylim(0,100)
W_old = [[0.1], [0.5]]
b_old = 0.5
while(count != 100):
    for i in range(100):
        if i < 50:
            pi = P1[i]
            ti = t1[i]
        if i >= 50:
            pi = P2[i-50]
            ti = t2[i-50]
        ai = Matrix_Multiplication(pi,W_old)[0][0] + b_old
        a = hardLim(ai)
        e = ti - a

        if e == 0:
            count+=1
        else:
            W_new = []
            for i in range(len(W_old)):
                W_new.append(W_old[i][0] + e*pi[0][i])
            W_old = W_new
            b_old += e
print(W_old)
print(b_old)