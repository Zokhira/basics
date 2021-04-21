# If statements:
# if expression:
#  code here when expression is True
# else:
#   code here when expression is False
'''
num1 = 2
num2 = 3
if num1 < num2:
    print("expression is true")
    print("you can do something here")
else:
    print("expression is false")

print("if statement completed here")


print("exercise: ----------------- ")
'''

nums = [45, 4, 5, 6, 3, 10, 5, 123, 346, 4, 5, 666, 5]
count = 0
# print values but when you find 5 , print it and print 'completed'
# for num in nums:
#    if num == 5:
#       print(num, 'completed')
#   else:
#        print(num, "is not 5")

for num in nums:
    if num == 5:
        count = count + 1  #count += 1
        print(count)

       # print(num, 'completed')
   # else:
     #   print(num, 'is not 5')

    



