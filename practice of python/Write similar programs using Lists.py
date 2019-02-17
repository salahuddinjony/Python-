matrix1=[[10,11,12],
         [13,14,15],
         [16,17,118]]
matrix2=[[1,2,3],
         [4,5,6],
         [7,8,9]]
matrix=[[0,0,0],
         [0,0,0],
         [0,0,0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        matrix[i][j]=matrix1[i][j]+matrix2[i][j]
for r in matrix:
    print(r)
