element="abcdaab"
b=""
c=[]
count=0
for i in element:
    if i not in b:
        b=b+i
for i in b:
    for j in element:
        if i==j:
            count+=1
    c.append(count)
    print(i,"-->",count,end=" ")
    count=0                   
