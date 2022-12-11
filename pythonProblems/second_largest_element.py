arr=[6,9,9,3,7,10,4]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]<arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
temp=arr[0]
while arr[i]<temp:
    i=+1
    break
print(arr[i])
        