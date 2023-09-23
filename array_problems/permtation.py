def permutation(lst):
    l=[]
    
    for i in range(len(lst)):
        m=lst[i]
        mxxx=lst[:i]+lst[i+1:]
   
        for p in permutation(mxxx):
            l.append([m]+p)
    return l
a=[1,2,3]
for p in permutation(a):
    print(p)
            