# Write your solution here
def transpose(matrix: list):
    n = len(matrix)
    # Create a new transposed matrix
    transposed = [[matrix[j][i] for j in range(n)] for i in range(n)]
    
    # Copy the transposed values back into the original matrix in place
    for i in range(n):
        for j in range(n):
            matrix[i][j] = transposed[i][j]