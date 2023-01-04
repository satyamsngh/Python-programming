
arr=[4,6,8,2,5,7]
n=len(arr)
# inter changing the position of there position  
# swiping the element 
for i in range(0,n-1,2):
    arr[i],arr[i+1]=arr[i+1],arr[i]
    print(arr[i],arr[i+1],end=" ")
   
