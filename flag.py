n=int(input("enter a number:"))
flag=0
if(n>0 and n<20):
    flag=1
    if(n%2==0):
        print("weird number")
    else:
        print("normal number")
if(n>=20 and n<30):
    flag=1
    print("normal number")
if(n>=30 and n%2==1):
    flag=1
    print("normal number")
else:
    flag=1
    print("weird number")
if(flag==0):
    print("invalid input")
