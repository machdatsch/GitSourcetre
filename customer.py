from vehicle import *
from random import randint
class Customer(object):
    
    def __init__(self,name):
    ######## CODE MISSING HERE
        self.__name = name
        self.__score = int


    def __str__(self):
    ######## CODE MISSING HERE
        return "Customer: " + self.__name

    def credit_score(self):
    ######## CODE MISSING HERE
        self.__score = randint(0,100)
        if self.__score:
            return True
        else:
            return False

    def get_score(self):
    ######## CODE MISSING HERE
        return self.credit_score()

class VIP_Customer(Customer):

    def credit_score(self):
    ######## CODE MISSING HERE
        return True

### test cases ###

# initialising customer instances

Wendy = Customer("Wendy")
Heidi = VIP_Customer("Heidi")

# print(Wendy) # expected output: Customer: Wendy
# print(Heidi) # expected output: Customer: Heidi

# print(Wendy.get_score()) # expected output: True or False depending on random score
# print(Heidi.get_score()) # expected output: True
