arr=[4,7,2,8,1,5,6,9]
n=len(arr)
a=[]
arr.sort()
i=0
#ascending
while (i<n/2):
   a.append(arr[i])
   i =i + 1
j=n-1   
#descending
while j>=n/2:
    a.append(arr[j])
    j=j-1
print(a)   