n=6
for i in range(n):
    for j in range(n-i):
        if i==(n-j-1):
            print(1+i,end=" ")
        else:
            print(" ",end=" ")
               
    for k in range(i):

        if i==k+1:
            print("1",end=' ')
        elif i==k+2:
            print("2",end=' ')    
                
        else:    
            print("*",end=' ')
    for  l in range(i):
       if i==l+1:
        print(i+1,end=" ")
       else:
        print("*",end=" ") 
    print()    