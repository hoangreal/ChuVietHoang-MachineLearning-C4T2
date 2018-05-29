import numpy as np
import cv2

def Matrix_Multiplication(A,B):
    r1 = A.shape[0]
    c1 = A.shape[1]
    r2 = B.shape[0]
    c2 = B.shape[1]
    if c1 == r2:
        result = np.array([[0 for j in range(c2)] for i in range(r1)])
        for k in range(c2):
            for i in range(r1):
                for j in range(r2):
                    result[i][k] += A[i][j]*B[j][k]
        return result

I = cv2.imread("D:\\PyCharm Community Edition 2018.1.3\\C4T Techkids\\Image Processing\\Image\\Lenna.png")
gray = cv2.cvtColor(I, cv2.COLOR_RGB2GRAY)
cv2.imshow("Old gray", gray)
shape_gray = gray.shape
#I will take 2*3 Matrixes and save them into a 'temp' array
A = np.array([
    [1, 0, 1],
    [-2, 0, 2],
    [1, 0, 1]
])
B = np.array([
    [-1, -2, 1],
    [0, 0, 0],
    [1, 2, 1]
])
C = np.array([
    [0, -1, 0],
    [-1, 4, -1],
    [0, -1, 0]
])
temp = np.array([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
])
n = input("Choose A,B,or C: ")
if n == 'A' or n == 'B' or n == 'C':
    if n == 'A':
        if shape_gray[0] % 3 == 0 and shape_gray[1] % 3 == 0:
            for row in range(3, shape_gray[0], 3):
                for col in range(3, shape_gray[1], 3):
                    gray[row-3:row, col-3:col] = Matrix_Multiplication(gray[row-3:row, col-3:col], A)
        else:
            remain_row = shape_gray[0] % 3
            remain_col = shape_gray[1] % 3
            for row in range(3,shape_gray[0],3):
                for col in range(3,shape_gray[1],3):
                    gray[row-3:row, col-3:col] = Matrix_Multiplication(gray[row-3:row, col-3:col], A)
            for row in range(shape_gray[0]-remain_row+0,shape_gray[0]):
                gray[row:shape_gray[0], 0: shape_gray[1]] = 0
            for col in range(shape_gray[1]-remain_col+0, shape_gray[1]):
                gray[0:shape_gray[0], col:shape_gray[1]] = 0

    elif n == 'B':
        if shape_gray[0] % 3 == 0 and shape_gray[1] % 3 == 0:
            for row in range(3, shape_gray[0],3):
                for col in range(3, shape_gray[1],3):
                    gray[row-3:row, col-3:col] = Matrix_Multiplication(gray[row-3:row, col-3:col], B)
        else:
            remain_row = shape_gray[0] % 3
            remain_col = shape_gray[1] % 3
            for row in range(3, shape_gray[0],3):
                for col in range(3, shape_gray[1],3):
                    gray[row-3:row, col-3:col] = Matrix_Multiplication(gray[row-3:row, col-3:col], B)
            for row in range(shape_gray[0]-remain_row+0, shape_gray[0]):
                gray[row:shape_gray[0], 0: shape_gray[1]] = 0
            for col in range(shape_gray[1]-remain_col+0, shape_gray[1]):
                gray[0:shape_gray[0], col:shape_gray[1]] = 0
    else:
        if shape_gray[0] % 3 == 0 and shape_gray[1] % 3 == 0:
            for row in range(3, shape_gray[0],3):
                for col in range(3, shape_gray[1],3):
                    gray[row-3:row, col-3:col] = Matrix_Multiplication(gray[row-3:row, col-3:col], C)
        else:
            remain_row = shape_gray[0] % 3
            remain_col = shape_gray[1] % 3
            for row in range(3,shape_gray[0],3):
                for col in range(3,shape_gray[1],3):
                    gray[row-3:row, col-3:col] = Matrix_Multiplication(gray[row-3:row, col-3:col], C)
            for row in range(shape_gray[0]-remain_row+0,shape_gray[0]):
                gray[row:shape_gray[0], 0: shape_gray[1]] = 0
            for col in range(shape_gray[1]-remain_col+0, shape_gray[1]):
                gray[0:shape_gray[0], col:shape_gray[1]] = 0
cv2.imshow("New gray", gray)
cv2.waitKey()








