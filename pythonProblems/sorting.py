#selection sort
arr=[64,25,12,22,11]
n=len(arr)
for i in range(n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print(arr)

#bubble sort
for i in range(n):
        for j in range(0, n-i-1):
            #leave the last element because it is sorted with itteration
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)                