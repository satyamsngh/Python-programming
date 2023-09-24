n=13
a=[]
for i in range(n):
    if i==2:
        a.append(i)
    if i>2:
        for j in range(2,i):
            if i%j==0:
                print(i)
                break
        else:
            a.append(i)

print(a)   