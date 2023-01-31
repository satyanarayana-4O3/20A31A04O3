a=int(input("enter day:"))#days
b=int(input("enter no of calls:"))#calls
c=int(input("enter no of messages:"))#messages
d=float(input("data used: "))#data
test= 0<=a<=84 and 0<=b<=3000 and 0<=c<=100 and 0<=d<=2.0
if test:
    f=84-a
    print("days left:",f)
    g=3000-b
    print("calls left :",g)
    h=100-c
    print("messages left : ",h)
    i=2.0-d
    print("remaining data",i,"gb")
else:
    print("your recharge pack is over")

