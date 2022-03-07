a=[[1,2,3],[4,5,6]]
b=[[0,0],[0,0],[0,0]]
for i in range(3):
    for y in range(2):
        b[i][y]=a[y][i]
print(b)