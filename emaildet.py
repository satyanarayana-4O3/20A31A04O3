email="vinil@gmail.com"
password=12345
cemail=input("enter the mail:")
cpassword=int(input("enter the password:"))
if(email==cemail and password==cpassword):
    print("login succuessfuly")
elif(email!=cemail and password==cpassword):
    print("invalid email")
elif(email==cemail and password!=cpassword):
    print("invalid paasword")
elif(email!=cemail and password!=cpassword):
    print("both are invalid")
else:
    print("invalid details",end=' ')
    print("login failed")
    
