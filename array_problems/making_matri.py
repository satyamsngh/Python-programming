b=5
c=[[ 0 for i in range (b)]for j in range (b)]
for i in range(b):
    for j in range(b):
        if i==0:

            print(j+1,end=' ')
        else:
            print(0,end=" ")    
    print()        
