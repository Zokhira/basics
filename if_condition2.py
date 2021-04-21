#         03/14/2021 If statements (continue)
'''
num = 2
if num >= 1:
    print(f"number is equal or greater than 1")
else:
    print(f"number is less than 1")

# expression AND/OR
'''

# age = int(input('enter the visitors age: '))
age = 3
if 0 <= age <= 4:
    print("Your admission cost $0.")
elif 4 < age < 18:
    print("Your admission cost is $5.")
elif 18 <= age < 140:
    print("Your admission cost is $10.")
else:
    print("Invalid age was entered, bye!")

age = int(input('enter the visitors age: '))
price = 0
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 140:
    price = 10
else:
    print("Invalid age was entered, bye!")
print(f"Your admission cost is ${price}.")


alien_color =input('enter the alien color (green/yellow/red): ')
if alien_color == 'green':
    print(f"You just earned 5 points!!")
elif alien_color == 'yellow':
    print(f"You just easrned 2 points, whee!")
elif alien_color == 'red':
    print(f"You just earned 10 points, you are killing it, man!!")
else:
    print("no points, sorry, take a rest, meditate.")


num = int(input('enter the users answer: '))
if num / 3:
    print("Fuzz")
elif  num / 5:
    print("Buzz")
elif num / 3 and 5:
    print("FuzzBuzz")
else:
    print("don't worry maybe next time you will do better:)")
