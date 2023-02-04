#program to create self arg and access an obj
class abc:
    class_var=0
    def _init__(self,var):
        abc.class_var+=1
        self.var=var
        print("the obj value is",var)
        print("the class value is",abc.class_var)
obj1=abc(100)
obj2=abc(101)
obj3=abc(102)
