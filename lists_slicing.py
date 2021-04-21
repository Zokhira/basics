# 03/13/2021
# Working with part of the list
cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
# slice of the list list_name[start:stop] - start is inclusive, stop is exclusive values
# values: list_name[start], list_name[stop-1]
for car in cars [1:3]:
    print(f" the car is: {car}")

print(" -----------------------second-----------------")
for car in cars[:3]: # the same thing as cars [0:3]
    print(f" the car is: {car}")

print(" -----------------------third-----------------")
for car in cars[2:]: # the same thing as cars [2: end of the list]
    print(f" the car is: {car}")

print(" -----------------------fourth-----------------")
for car in cars[2:10]: # no Index out of range error
    print(f" the car is: {car}")

print("-------copying and linking---------")
print("-------linking---------")
cars2 = cars
print(f"cars: {cars}")
print(f"cars2: {cars2}")
cars.append('bmw')
print(f"cars after update: {cars}")
print(f"cars2 after update: {cars2}")

print("-------copying---------")
cars3 = cars[:]
print(f"cars: {cars}")
print(f"cars3: {cars3}")
cars.append('toyota')
print(f"cars after update: {cars}")
print(f"cars3 after update: {cars3}")

print("Exercise 4-10: slicing")
print(f"The first three items in the list are: {cars[:3]}")
print(f"Three items  from the middle of the list are: {cars[2:5]}")
print(f"The last three items in the list are: {cars[3:]}")

# Lists can be modified (mutable)
# Tuples - data structure similar to list but can be modified (immutable)
cars_t = ('bugatti', 'ferrari', 'tesla', 'lexus')
