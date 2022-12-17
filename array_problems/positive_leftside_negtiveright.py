def posrightside(arr,n):
    i=-1
    for j in range(n):
       if arr[j]<0:
         i+=1
         arr[i],arr[j]=arr[j],arr[i]
    print(arr)

def posleftside(arr,n):
    i=-1
    for j in range(n):
        if arr[j]>0:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    print(arr)       
    

arr=[10, 7, -11, -9, 1, -5]
n=len(arr)   
posrightside(arr,n)
posleftside(arr,n)
