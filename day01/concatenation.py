
git

print('My name is ' + name)
print('My age is ' + str(age))
# to concatenate variable in Python format function is recommended.
print('My age is {}'.format(age))
# f format is an easy way
print(f'My name is {name} and I am {age} years old')
# another way
print('Python', 3, 'is awesome:', True)

print('--------------------------------------')

#input("Press Enter to Exit")

#print(input('Check') + ' pass')

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
sum = num1 + num2
print('The sum of {} and {} is {}'.format(num1, num2, sum))