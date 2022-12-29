#finding the sum
arr=[1,7,2,15]
n=len(arr)
target=9
t=[]
for i in range(n-1):
    for j in range(i+1,n):
        if arr[i]+arr[j]==target:
            t.append(arr[i])
            t.append(arr[j])
print(t) 



#median of two array
arr1=[1,2]
arr2=[3,4,5]
for i in range(len(arr2)):
    arr1.append(arr2[i])
print(arr1)
n=len(arr1)
median=n//2
print(median)
if n%2!=0:
    print(arr1[n//2])
else:
    print((arr1[median-1]+arr1[median])/2)





