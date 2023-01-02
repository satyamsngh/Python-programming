a=[4,7,4,9]
b=[2,5,6,8]
for i in range(len(b)):
    a.append(b[i])
print(a)
a.sort()
print(a)
n=len(a)//2
if len(a)%2 != 0:
    print(a[n])
else:
    add=(a[n]+a[n-1])/2
    print(add)