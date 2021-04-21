

# H/W print multiplication table

num = 10
for n in range (1, 11):
    print(num,'x',n,'=', num*n)

print('************************list of dictionaries ***********************')
#buser_0 = {'name': }

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
names = {'john': 'java', 'zara': 'html', 'sarah': 'c', 'seva': 'python', 'edward': 'ruby'}
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")