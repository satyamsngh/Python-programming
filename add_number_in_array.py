def add_number(arr):
    l=len(arr)-1
    b=12
    for i in range(0,l):
        for j in range(i+1):
            if arr[i]+ arr[j]==b:
                index= arr[i],arr[j]
    return ("index is :",index)  

arr=[1,3,7,5,4]    
print(add_number(arr))      
