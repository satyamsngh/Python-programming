array=[5,6,8,6,6,1,10]
n=len(array)
max=array[2]
min=array[2]
l=[]
for i in range(n):
    if min >= array[i]:
        min=array[i]
    if max <= array[i]:
         max=array[i]
l.append(max)
l.append(min)

print(l)