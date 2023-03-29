arr=[10, 7, 11, 9, 1, 5]
n=len(arr)
max=arr[0]
for i in range(1,n):
    if arr[i]>max:
        #printing max value
        max=arr[i]
print(max)                

