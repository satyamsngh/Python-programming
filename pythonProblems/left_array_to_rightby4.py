arr=[3,5,6,2,5,0]
d=4
n=len(arr)
temp=[]
for i in range(d,n):
    temp.append(arr[i])
for i in range(d):
    temp.append(arr[i])
print(temp)    