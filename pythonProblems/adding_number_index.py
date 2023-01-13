arr=[3,6,7,8,9]
j=1
new=[]
#adding two index value
for i in range(len(arr)-1):
    new.append(arr[i]+arr[i+j])
print(new)