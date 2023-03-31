def recursion(list):
    #recursion
    if len(list)==1:
        return list[0]
    return list[0]+recursion(list[1:])
print(recursion([1,4,3,5,7,4]))