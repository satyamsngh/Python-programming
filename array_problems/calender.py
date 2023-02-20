row=3
column=7
count=7
a=[" ","1","2","3","4","5","6"]
for i in range(1):
    for j in range(column):
        print(a[j],end=" ")
    print()    
for i in range(row):        
    for j in range(column):
        print(count,end=" ")
        count+=1
    print()    