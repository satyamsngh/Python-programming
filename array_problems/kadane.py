arr=[1,2,3,-2,5]
n=len(arr)
mx=arr[0]
max_value=0
count=0
#this loop if all the element is negative
for i in range(n):
    if arr[i]<0:
        count+=1
if count==n:
    arr.sort()
    print(arr[n-1])

#this is for all the combination of positive and negative
for i in range(n):
    max_value+=arr[i]
    if max_value<0:
        max_value=0
    mx=max(mx,max_value)
print(mx)    
