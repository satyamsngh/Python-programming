a=65
n=5
#print alphabet
for i in range(n):
    for j in range(i+1):
        print(chr(a),end=" ")
        a=a+1
    print()  