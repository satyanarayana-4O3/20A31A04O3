#constructor
class Employee:
    def __init__(self,name,id):
        self.id=id
        self.name=name
    def display(self):
        print("ID :%d \n name:%s" %(self.id,self.name))
emp1=Employee("john",101)
emp2=Employee("david",102)

emp1.display()
emp2.display()

