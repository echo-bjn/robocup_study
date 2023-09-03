X=eval(input("请输入矩阵X:"))
Y=eval(input("请输入矩阵Y:"))
Z=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(X)):
    for j in range(len(Y)):
        Z[i][j]=X[i][j]+Y[i][j]
print(Z)