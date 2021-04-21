# Functions available for string
fullname = "John Doe"
msg = "we are looking at string functions in python."
print(fullname)
print(fullname.upper())
print(fullname.title())
print(msg.replace('.','!!!!').title())
print(msg.replace('python','java'))

# Concatenation
msg1 = fullname.title() + "," + msg
print(msg1)
print(fullname.upper() + "," + msg)

# working with whitespaces in string: \t, \n, esc, etc.
msg2 = fullname.upper() + "\n\t\t\t, " + msg
print(msg2)
msg3 = '\n\t\t\t' + fullname.upper() + ", " + msg
# str. strip() - removes leading and preceding whitespace
print(msg3 + ' !!! ')
print(msg3.strip() + ' !!! ')

 #fstring
msg4 = f"{fullname.upper()}, {msg}"
print("fstring")

num = 400
num2 = 600
print(num + num2)
print(f"num + num2 = {num + num2}")
print(num - num2)

print(f"3**2 = {3**2}")

num4 = "45.55"
print(f"num + num2 = {num + float (num4)}")

print(int(45.4988))
print(f"fullname.isdigit() >> {fullname.isdigit()}")


course = 'Python for beginners'
print(course[:])

first = 'Zoya'
last = 'Aziza'
message = first + ' [' + last + '] is a coder.'
print(message)

msg = f'{first} [{last}] is a coder.'
print(msg)

course = 'Python for beginners'
print(len(course))
course = "Python for beginners"
print(course.upper())
print(course.lower())
print(course.title())
print(course)
print(course.find('P'))
print(course.replace('beginners', 'Absolute Beginners'))
print('Python' in course)