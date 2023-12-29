print("Enter the required rows and coloumns:-")
m,n=input().split(" ")
a=int(m)
b=int(n)

matrix=[]
print("Enter the elements:-")

for i in range(a):
    c=[]
    for j in range(b):
        c.append(int(input()))
    matrix.append(a)
    
for i in range(a):
    for j in range(b):
        print(matrix[i][j], end=" ")
    print()