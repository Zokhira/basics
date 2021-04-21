'''
name = input('What is your name? ')
favorite_color = input('What is your favorite color? ')
print(name + ' likes ' + favorite_color)
birth_year = input('Birth year: ')
age = 2021 - int(birth_year)
print(age)
weight_lbs = input('Weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)
'''

course = 'Python for beginners'
print('Python' in course)

print(10 ** 3)
x = 10
x -= 3
print(x)

x = (10 + 3) * 2 ** 2
print(x)

x = (2 + 3) * 10 - 3
print(x)

print('Zohira'[5])

x = 2.9
print(abs(-2.9))
'''
is_hot = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
else:
    print("It's a cold day")
    print("Wear warm clothes")
print("Enjoy your day")
'''
is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")

'''
has_high_income = False
has_good_credit = True
if has_high_income and has_good_credit:
    print("Eligible for loan")
'''

has_good_credit = True
has_criminal_record = True
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")


temperature = 30
if temperature != 30:
    print("It's a hot day")
elif temperature < 30:
    print("It's a cold day")
else:
    print("It's neither hot nor cold")

name = "John Smith"
if len(name) < 3:
    print("Name must be at least 3 characters.")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good!")
'''
weight = int(input('Weight: '))
unit = input('(L)bs or (k)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")
'''
i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
print("Done")

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print("Sorry, you failed!")
