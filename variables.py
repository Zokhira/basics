# naming the file: avoid spaces, avoid upper cases, '_' can be used to separate words
# new_variables.py (python), newVariables.java (java)
# Variables:
# naming: should not start with numbers, starts with lower case, symbols and numbers can be used
# nameofthevariable = value, declaring and defining (setting a value for the variable)
vname = 'john doe' #  or "Zokhira" # string data type
num = 12 # Integer date type
status = True # or False # Boolean data type
price = 45.789 # double/float data type
message = "Hello class, we are starting to learn python!!"

print ("Hello Again!")
print (vname)
print (num)
print ("--------------")

vname = 'jane doe' # I am resetting the value of vname variable
num = 9876
print (vname, "***", num, status, price, message)
# NameError: name 'num' is not defined - this means 'num' variable is not created before this line

# Data types: String (str), Integers (Int), floats (float), boolean (bool)-true/false
a = 'john doe'
b = 5 # num1 = 5
c = 10 # num2 = 10

# Exercise: 2.1
message = 'This is the message for exercise 2.1'
print(message)
# Exercise: 2.2
message = 'new message for exercise 2.2'
print(message)

places_to_go = ['italy', 'spain', 'france', 'sweden', 'finland']
print(places_to_go)
places_to_go.sorted()
print(places_to_go)
places_to_go.sorted(reverse=True)
print(places_to_go)
places_to_go.reverse()
print(places_to_go)
places_to_go.sorted.asc()
print(places_to_go)
places_to_go.reverse.desc()
print(places_to_go)