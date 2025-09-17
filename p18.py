#matrix

matrix=[ 
    [1,2,3],
    [4,5,6],
]

print(matrix[0][2])

#change valu

matrix[0][2]=12
print(matrix[0][2])

for row in matrix:
    for col in row:
        print(col)