#write a python program to perform matrix addition, matrix subtraction and matrix multiplication by simualting matrix as a list of lists. you may use separate functions for each operation.
def matrix_addition(mat1, mat2):
    if len(mat1)!=len(mat1) or len(mat1[0]) != len(mat2[0]):
                                   
                                   print("Error: Matrices must have the same dimensions for matrix addition..")
                                   return None
    result = [[0 for _ in range(len(mat1[0]))] for _ in range(len(mat1))]
    for i in range (len(mat1)):
        for j in range (len(mat1[0])):
            result[i][j] = mat1[i][j] + mat2[i][j]
    return result

def matrix_subtraction(mat1, mat2):
    if len(mat1)!=len(mat1) or len(mat1[0]) != len(mat2[0]):
                                   print("Error: Matrices must have the same dimensions for matrix subtraction..")
                                   return None
    result = [[0 for _ in range(len(mat1[0]))] for _ in range(len(mat1))]
    for i in range (len(mat1)):
        for j in range (len(mat1[0])):
            result[i][j] = mat1[i][j] - mat2[i][j]
    return result

def matrix_multiplication(mat1, mat2):
    #check if matrices can be multiplied, no. of columns in mat1 = no. of rows in mat2
    if len(mat1[0]) != len(mat2):
           print("Error: Number of cilumns in first matrix must be equal to number of rows in second matrix for multiplication..")
           return None
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
    for i in range (len(mat1)):
        for j in range (len(mat2[0])):
            for k in range (len(mat2)):
                result[i][j] += mat1[i][k]*mat2[k][j]
    return result

#example matrices
matrix_a = [[1,2,3],[4,5,6],[7,8,9]]
matrix_b = [[9,8,7],[6,5,4],[3,2,1]]

#Matrix Addition
result= matrix_addition(matrix_a,matrix_b)
print("Matrix Addition")
print(result)

#Matrix subtraction
result= matrix_subtraction(matrix_a,matrix_b)
print("Matrix Subtraction")
print(result)

#Matrix Multiplication
result= matrix_multiplication(matrix_a,matrix_b)
print("Matrix Multiplication")
print(result)

