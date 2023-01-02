n=int(input("enter the number:"))
for i in range(n):
    for j in range(i+1):
        if i==j:
            print("1",end=' ')
        else: 
            print(" ",end=' ')
    for l in range(n-i-1):
        print(" ",end=' ')
    for m in range(n-i-1):
        if i==(n-2-m):
            print("1",end=" ")
        else:
            print(" ",end=' ')    

    print() 
for j in range(n-1):
    for k in range(n-j-1):
        if (n-2-k)==j:
            print("1",end=" ")    
        else:    
            print(" ",end=' ')
    for o in range(j+1): 
            print(" ",end=' ') 
    for p in range(i+1):
        if p==j:
            print("1",end=' ') 
        else:
            print(" ",end=' ') 
                              
    print()                 