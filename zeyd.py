import math
import numpy as np

def Solve(A, b, eps, max_iterations = 100):
    n = len(b)
    d = [b[i] / A[i][i] for i in range(n)]
    C = A
    

    for i in range(n):
        temp = C[i][i]
        for j in range(n):
            C[i][j] = (C[i][j] / temp) * -1
        C[i][i] = 0
    print(C)
    print(d)

    x = d.copy()
    x_prev = d.copy()
    
    for k in range(max_iterations):
        max_error = 0     
        for i in range(n):
            sum = 0
            temp = 0
            for j in range(i):
                temp += A[i][j] * x[j]
            sum += temp
            temp = 0
            for j in range(i + 1, n):
                temp += A[i][j] * x_prev[j]
            sum += temp
            x[i] = b[i] + sum
            error = abs(x[i] - x_prev[i])
            max_error = max(max_error, error)
        x_prev = x.copy()
        print(max_error)
        if max_error < eps: 
            return x
        print(f"Ітерація ({k+1}): {x}")
    print("СЛАР не збігся")
    return



if __name__ == "__main__":
    A = [
        [-0.83, 0.31, -0.18, 0.22],
        [-0.21, -0.67, 0, 0.22],
        [0.32, -0.18, -0.95, -0.19],
        [0.12, 0.28, -0.14, -1]
    ]

    b = [1.71, -0.62, 0.89, -0.94]

    
    eps = 0.001
    print(Solve(A, b, eps))