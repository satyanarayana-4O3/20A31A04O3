#variable and var.access in class and method
class computer():
    a=10
    b=20
    print("class variables inside class",a)

    def config(self):
        c=100
        print("yes")
        print("instance access",self.b)
lenova=computer()
print(lenova.a)
print(lenova.a+lenova.b)
dell=computer()
print("dell",dell.a)
lenova.config()
