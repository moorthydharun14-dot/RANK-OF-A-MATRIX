#Program to find the rank of a matrix.
#RegisterNumber: DHARUN M 25018453
#RegisterNumber: 212225230057
import numpy as np
matrix = np.array([[1,2,3],[3,6,9]])
rank = np.linalg.matrix_rank(matrix)
print(rank)
