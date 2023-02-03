str1='silent'
str2='listen'
n=len(str1)
m=len(str2)
sortedstr1=sorted(str1)
sortedstr2=sorted(str2)
if n==m:
    if sortedstr1==sortedstr2:
        print("anagram")
    else:
        print("not")
else:
    print("not")
