n=6
b=[[0 for i in range(n)]for j in range(n-1)]

count=1
for i in range(n):
    for j in range(n-1):
        b[j][i]=count
        count=count+1    
        
    
    
            
        
for i in range(n-1):
    for j in range(n):
        print(b[i][j],end=' ')
    print()
print("31")    
        