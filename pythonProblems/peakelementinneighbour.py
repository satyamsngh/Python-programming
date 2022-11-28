def peakelement(arr,n):
    for i in range(0,n-1):
        if(arr[i]>=arr[i-1] and arr[i]>=arr[i+1]):
            return arr[i]


arr=[5, 10, 20, 15]
n=len(arr)
print(peakelement(arr,n))
        