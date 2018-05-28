import numpy as np
import cv2

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

I = cv2.imread("D:\\C4T Techkids\\Image Processing\\Image\\Building.jpg")
gray = cv2.cvtColor(I,cv2.COLOR_RGB2GRAY)
cv2.imshow("Old gray",gray)
a = gray.shape
#I will take 2*3 Matrixes and save them into a 'temp' array
A = np.array([
    [1,0,1],
    [-2,0,2],
    [1,0,1]
])
B = np.array([
    [-1,-2,1],
    [0,0,0],
    [1,2,1]
])
C = np.array([
    [0,-1,0],
    [-1,4,-1],
    [0,-1,0]
])

n = input("Choose A,B,or C: ")
if n == 'A' or n == 'B' or n == 'C':
    if n == 'A':
        for row in range(2,a[0],2):
            for col in range(3,a[1],3):
                gray[row-2:row, col-3:col] = Matrix_Multiplication(gray[row-2:row,col-3:col],A)
    elif n == 'B':
        for row in range(2, a[0], 2):
            for col in range(3, a[1], 3):
                gray[row - 2:row, col - 3:col] = Matrix_Multiplication(gray[row - 2:row, col - 3:col], B)
    else:
        for row in range(2, a[0], 2):
            for col in range(3, a[1], 3):
                gray[row - 2:row, col - 3:col] = Matrix_Multiplication(gray[row - 2:row, col - 3:col], C)
cv2.imshow("New gray",gray)
cv2.waitKey()








