import numpy as np

# Create two matrices
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

# Matrix addition
C = A + B

# Matrix subtraction
D = A - B

# Matrix multiplication
E = np.dot(A, B)

# Element-wise multiplication
F = A * B

# Print the results
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Addition (A + B):\n", C)
print("Subtraction (A - B):\n", D)
print("Matrix multiplication (A @ B):\n", E)
print("Element-wise multiplication (A * B):\n", F)