n=6
count=1
b=[[0 for i in range(n)]for j in range(n)]
for i in range (n):
    for j in range(n):
        b[j][i]=count
        count+=1
        
for i in range(n):
    for j in range(n-1):
        print(b[i][j],end=' ')
    print()            
