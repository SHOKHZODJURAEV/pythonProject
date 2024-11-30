from utility import minus, concat
import utility as ut




print(minus(12, 6))



print(concat('Test', 'test'))



print(minus(50, 25))



print('---------------------------------------------')


total = 0
for number in range(1, 6):
    total += number
print(total)

s = "Python"

for b in s[::-1]:
    print(b)

for i in range(0, 100):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


