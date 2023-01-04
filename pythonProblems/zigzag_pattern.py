n=3
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(i+1):
        if k==0:
           print("*",end=" ")
        else:
            print(" ",end=" ") 
    for l in range(i):
        if i==l+1:
            print("*",end=" ")              
        else:
            print(" ",end=" ")
    for q in range(n-i-1):
        print(" ",end=" ")
    for p in range(n-i-1):
        if i==n-p-2:
            print("*",end=" ") 
        else:
            print(" ",end=" ") 
    for w in range(i):
        print(" ",end=' ')
    for s in range(i):
        if i==s+1:
            print("*",end=" ")              
        else:
            print(" ",end=" ")                  
    print()