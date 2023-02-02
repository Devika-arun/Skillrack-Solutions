r, c = map(int, input().split())

mat = [[0]*c for _ in range(r)]
#input of a matrix
for i in range(r):
    mat[i] = [int(j) for j in input().strip().split(" ")]

#swapping of First and Last row
temp1 = [0]*(c) #for storing the swapping row elements

for i in range(1):
    for j in range(c):
        temp1[j] = mat[i][j]
        mat[i][j] = mat[r-1][j]
        mat[r-1][j] = temp1[j]
       
#swapping of First and Last col
temp2 = [0]*r #for storing the swapping column elements

for i in range(r):
    for j in range(1):
        temp2[i] = mat[i][j]
        mat[i][j] = mat[i][c-1]
        mat[i][c-1] = temp2[i]

print("After swapping: ")
for i in range(r):
    for j in range(c):
        print(mat[i][j], end = " ")
    print("")
