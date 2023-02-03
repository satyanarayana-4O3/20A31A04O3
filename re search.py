import re
str1="she sells sea shells at sea shore"
p1="sells"
if re.search(p1,str1):
    print("match found")
else:
    print(p1,"not present in the string")
p2="she"
if re.search(p2,str1):
    print("match found")
else:
    print(p2,"not present in the string")
