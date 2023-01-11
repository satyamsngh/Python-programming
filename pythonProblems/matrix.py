n=3
k=(2*n)-1
low=0
high=k-1
value=n
#adding the value in the matrix
matrix=[[0 for i in range(k)] for j in range(k)]
for i in range(n):
    for j in range(low,high+1):
        matrix[i][j]=value
    for j in range(low+1,high+1):
        matrix[j][i]=value
    for j in range(low+1,high+1):
        matrix[high][j]=value
    for j in range(low+1,high):
        matrix[j][high]=value        
        

    low+=1
    high-=1
    value-=1
    #printing the matrix     
for i in range(k):
    for j in range(k):
        print(matrix[i][j],end=' ')
    print()    