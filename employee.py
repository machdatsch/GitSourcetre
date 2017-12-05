from vehicle import *
from customer import *

class Employee(object):
    ######## CODE MISSING HERE
    emp_id = 0

    def __init__(self, name):
    ######## CODE MISSING HERE
        self.__name = name
        self.__id = Employee.emp_id + 1
        Employee.emp_id += 1

    def __str__(self):
    ######## CODE MISSING HERE
        return "Employee: " + self.get_name() + " is of type " + str(self.get_title())

    def get_name(self):
    ######## CODE MISSING HERE
        return self.__name
    
    def get_title(self):
    ######## CODE MISSING HERE
        return "Subordinate"
    
class Manager(Employee):

    def get_title(self):
    ######## CODE MISSING HERE
        return "Manager"

    def get_sales_report(self,salesman):
    ######## CODE MISSING HERE
        try:
            print(str(salesman)[10:-23] + "'s current cumulative sales:\n" + str(salesman.sales[str(salesman)[10:-23]]))
        except:
            raise KeyError("The salesman does not have any sales at this moment")

class Salesman(Employee):

    ######## CODE MISSING HERE
    sales = {}

    def sale(self,vehicle,sales_price,customer):
    ######## CODE MISSING HERE
        if customer.get_score():
            if self.get_name() in self.sales.keys():
                return self.sales.update({self.get_name():self.sales[self.get_name()] + sales_price})
            else:
                return self.sales.update({self.get_name():sales_price})
        else:
            return "The customer does not have enough cash!!!!"
        print(self.sales)

### test cases ###

## initialising employee instances

Eric = Manager("Eric")
Kyle = Employee("Kyle")
Stan = Salesman("Stan")
Kenny = Salesman("Kenny")
Craig = Salesman("Craig")

## printing employee instances

# print(Eric) # expected output: Employee: Eric is of type Manager
# print(Kyle) # expected output: Employee: Kyle is of type Subordinate
# print(Stan) # expected output: Employee: Stan is of type Subordinate
# print(Kenny) # expected output: Employee: Kenny is of type Subordinate
# print(Craig) # expected output: Employee: Craig is of type Subordinate


## registering sales

Kenny.sale(Veh2,6000,Heidi)

Stan.sale(Veh1,9000,Wendy)


## printing an individual sales report:

Eric.get_sales_report(Craig)
# expected output:
# Kenny's current cumulative sales:
# 6000
