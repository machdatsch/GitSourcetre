class Vehicle(object):
    ######## CODE MISSING HERE
    vehicle_id = -1
    vehicles_sold = []

    def __init__(self,year,mileage,purchase_price,serial_number):
    ######## CODE MISSING HERE

        self.__year = year
        self.__mileage = mileage
        self.__purchase_price = purchase_price
        self.__serial_number = serial_number
        self.check_validity()
        
    ######## CODE MISSING HERE

    def __str__(self):
    ######## CODE MISSING HERE
        return str(self.get_id())

    def check_validity(self):
        try:
            self.__year + 0
        except:
            raise ValueError("Value year is not allowed to be of type: " + str(type(self.__year)) + " please use type int")

        try:
            self.__mileage + 0
        except:
            raise ValueError("Value mileage is not allowed to be of type: " + str(type(self.__year)) + " please use type int")

        try:
            self.__purchase_price + 0
        except:
            raise ValueError("Value purchase_price is not allowed to be of type: " + str(type(self.__year)) + " please use type int")


    def get_id(self):
    ######## CODE MISSING HERE
        return self.generate_vehicle_id()

    @staticmethod
    def generate_vehicle_id():
    ######## CODE MISSING HERE
        Vehicle.vehicle_id += 1
        return Vehicle.vehicle_id + 100000

class Car(Vehicle):

    def __init__(self,year,mileage,purchase_price,serial_number,doors):
    ######## CODE MISSING HERE
        self.__year = year
        self.__mileage = mileage
        self.__purchase_price = purchase_price
        self.__serial_number = serial_number
        self.__doors = doors
        self.__wheels = 4
        self.check_validity()

    def check_validity(self):
        try:
            self.__year + 0
        except:
            raise ValueError("Value year is not allowed to be of type: " + str(type(self.__year)) + " please use type int")

        try:
            self.__mileage + 0
        except:
            raise ValueError("Value mileage is not allowed to be of type: " + str(type(self.__year)) + " please use type int")

        try:
            self.__purchase_price + 0
        except:
            raise ValueError("Value purchase_price is not allowed to be of type: " + str(type(self.__year)) + " please use type int")


class Lorry(Vehicle):

    def __init__(self,year,mileage,purchase_price,serial_number,wheels,doors=2):
    ######## CODE MISSING HERE
        self.__year = year
        self.__mileage = mileage
        self.__purchase_price = purchase_price
        self.__serial_number = serial_number
        self.__wheels = wheels
        self.__doors = doors
        self.check_validity()

    def check_validity(self):
        try:
            self.__year + 0
        except:
            raise ValueError("Value year is not allowed to be of type: " + str(type(self.__year)) + " please use type int")

        try:
            self.__mileage + 0
        except:
            raise ValueError("Value mileage is not allowed to be of type: " + str(type(self.__year)) + " please use type int")

        try:
            self.__purchase_price + 0
        except:
            raise ValueError("Value purchase_price is not allowed to be of type: " + str(type(self.__year)) + " please use type int")

        
class Motorcycle(Vehicle):

    ######## CODE MISSING HERE
    classic_count = 0

    def __init__(self,year,mileage,purchase_price,serial_number,classic=False):
    ######## CODE MISSING HERE
        self.__year = int(year)
        self.__mileage = mileage
        self.__purchase_price = purchase_price
        self.__serial_number = serial_number
        self.__classic = classic
        self.check_validity()

        if classic == True:
            Motorcycle.classic_count += 1

    def check_validity(self):
        try:
            self.__year + 0
        except:
            raise ValueError("Value year is not allowed to be of type: " + str(type(self.__year)) + " please use type int")

        try:
            self.__mileage + 0
        except:
            raise ValueError("Value mileage is not allowed to be of type: " + str(type(self.__year)) + " please use type int")

        try:
            self.__purchase_price + 0
        except:
            raise ValueError("Value purchase_price is not allowed to be of type: " + str(type(self.__year)) + " please use type int")
    

### test cases ###

# initialising vehicle instances
Veh1 = Vehicle(2008,65000,7500,"34567851g4")
Veh2 = Car(2007,125000,5500,"e44653ftu1",4)
Veh3 = Car(2012,45000,8900,"gf5622iguz",doors=2)
Veh4 = Lorry(2005,180000,16000,"hbh997123f",6)
Veh5 = Lorry(2013,30000,35000,"hjbf17jbkh",8,4)
Veh6 = Motorcycle("1975",75500,40000,"bh545664rh",True)
veh_list = [Veh1,Veh2,Veh3,Veh4,Veh5,Veh6]

# for veh in veh_list:
#     print(veh)

#prints     100000
#           100001  
#           100002  
#           100003  
#           100004  
#           100005


# Veh7 = Motorcycle("year",10000,25000,"bjhgss4rdh",False)
# instance Veh7 generates an exception (ValueError) (uncomment to test)
