# 1) How to swap 2 variable values i e.g.: If a=45 b=78 >> a=78 b=45 (by using flag)
a = 45
b = 78
print(a,b)

# Version 1:
# temp = a
# a = b
# b = temp
# print(a,b)

# Version 2:

a, b = b, a
print(a, b)

# 2) Count the vowels in any phrase/sentence/word. User enters any phrase, you return:
# number of print this statement: print(f"number of {vowel}'s is: {count}".)
'''
user_word = input('Please, write any word/phrase/sentence: ')
text = list(user_word)

vowels_count = 0

for i in text:
    if i in ('a', 'e', 'o', 'i', 'u'):
        vowels_count += 1
    else:
        pass
print(f"number of vowel's is: {vowels_count}")
'''

# 3) Count each letter in any phrase. (by using dictionary)
# Version 1:
user_word = 'hello there'
x = user_word.replace(' ', '')
print(x)
y = len(x)
print(y)

# Version 2:
# user_word = input('Please, write any word/phrase/sentence: ')
# count_letters = {}
# for i in user_word:
#     if i in count_letters:
#         count_letters[i] += 1
#     else:
#         count_letters[i] = 1
# print(f"number of letter's is: {count_letters}")

# 4) Find the first mostly used letter in a phrase. (max(),dictionary, if the key is in the dictionary, increment.)

# user_word = input('Please, write any word/phrase/sentence: ')
# find_mostly_used_letters = {}
# for i in user_word:
#     if i in find_mostly_used_letters:
#         find_mostly_used_letters[i] += 1
#     else:
#         find_mostly_used_letters[i] = 1
# max_value = max(find_mostly_used_letters, key = find_mostly_used_letters.get)
# print(f"mostly used letter is: {max_value}")

# Book h/w 7-8:
sandwich_orders = ['cheese sandwich','tuna sandwich', 'pastrami sandwich', 'roasted chicken sandwich']
finished_sandwiches = []
for i in sandwich_orders:
    print(f"I made your {i}.")
    #finished_sandwiches += i
    finished_sandwiches.append(i)
    for i in finished_sandwiches:
        print(f"This {i} was made.")

print('---------------------------------------------------------------------------------------------')
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self,name,age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog("Lucy",3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

print("---------------------------------------------------------------------")

class Restaurant:
    