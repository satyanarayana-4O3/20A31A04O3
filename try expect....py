#try,except and finally program
a=100
b=0
try:
    print(a/b)
except:
    print("please note number cant be divided by 0")

finally:
    print("resource closed")

a=10
try:
    b=int(input("enter a number"))
    print("resource open")
    print(a/b)
except ZeroDivisionError as e:
    print("please note number can't be divisible by 0",e)
except ValueError as e:
    print("invalid input",e)
except Exception as e:
    print("other error")
finally:
    print("resouce closed")

x=10
try:
    print("hello")
    if x%2!=0:
        raise Exception("x should b even number")
    else:
        print("x is even number..correct")
finally:
    print("bye")


class computer:
    def config(self):
        print("YES")
lenova=computer()
lenova.config()
dell=computer()
dell.config()
