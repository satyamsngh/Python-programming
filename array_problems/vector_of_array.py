a=[]
size=int(input("enter length of array:\n"))
for i in range(size):
    n=int(input("enter the array value:\n"))
    a.append(n)
print(a)
first=a[0]

front=a[0]
for i in range(1,size):
    a[i-1]=a[i]
a[size-1]=first
print(a)