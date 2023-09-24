digits=[1,6,8,9]
a=""
b=[]
for i in digits:
    a+=str(i)
a=str(int(a)+1)
for i in a:
    b.append(int(i))
print(b)   