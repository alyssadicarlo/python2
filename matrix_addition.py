matrix1 = [[1,3], [2,4]]
matrix2 = [[5,2], [1,0]]
added = []

for i in range(len(matrix1)):
    temp = []
    for j in range(len(matrix1)):
        temp.append(matrix1[i][j] + matrix2[i][j])
    added.append(temp)

print(added)