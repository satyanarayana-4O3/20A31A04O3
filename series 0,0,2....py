#0,0,2,1,4,2,6,3,8,4,10
val=int(input("enter the number:"))
x=0
y=0
for i in range(1,val+1):
    print(x,end=' ')
    print(y,end=' ')
    if(i%2!=0):
        x=x+2
    else:
        y=y+1
if(val%2!=0):
    print('{}\n term in the program is{}'.format(val,x-2))
else:
    print('{}\n term in the program is{}'.format(val,y-1))

