arr=("geeks","geek","gee")
str1=max(arr)
str2=min(arr)
longest_string=""
for i in range(0,len(str2)):
    if str1[i]!=str2[i]:
        break
    else:
        longest_string+=str2[i]
print(longest_string)        