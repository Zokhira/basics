# 04/03/2021
# This file is for executing the cars.py classes
from classes.cars import Car

#  Execution
# drive() we will not have an access to this function yet

# mycar = Car()  # Car is the class, mycar is an object...in this line we are creating instance of the (instantiation)
mycar = Car("BMW", "530xi", "black")
yourcar = Car("Lexus", "Lexus IS", "silver")

print("=====================================================")
mycar.get_description()
mycar.drive()
mycar.set_odometer_reader(50)
mycar.odo_reader = 20 # this is direct access to the instance variables
mycar.color = 'RED'
mycar.get_description()
# yourcar.do_something()
print("=====================================================")
yourcar.get_description()
yourcar.drive()
yourcar.set_odometer_reader(30)
yourcar.get_description()


print("--- Electric car instances ---------")
my_ev = ElectricCar("tesla", "model x", "blue")
my_ev.drive()
my_ev.get_description()
print('Battery size : ', my_ev.battery_size)
# mycar.battery_size # only child has battery_size attribute, parent does not see that attribute
# Car (state, behaviour) -> ElectricCar(state, behaviour)