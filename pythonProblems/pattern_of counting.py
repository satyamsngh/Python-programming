n=5
row=1
for i in range(n):
    val=1+i
    dec=n-1
    for j in range(i+1):
        print(val,end=' ')
        val=val+dec
        
    print()