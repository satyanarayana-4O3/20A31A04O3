size=int(input("enter the size of bin:"))
max=count=flag=0
x=input()
arr=list[x]
for i in range(0,size):
    if arr[i]=='1':
        count+=1
        flag=1
    elif (arr[i]=='0' and flag==1):
        count=0
        flag=0
    
    if count>max:
        max=count
        print(max)
