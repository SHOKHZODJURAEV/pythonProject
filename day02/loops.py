s = 'Python'
for each in s:
    print(each)

print('-------------------------------------------')

for i in range(1, len(s)):
    print(i)

print('---------------------Check-----------------------')

for i in range(-len(s),0):
    print(s[i])

print('----------------------Test-----------------------')

for i in reversed(range(len(s), 0)):
    print(s[i])
for b in s[::-1]:
    print(b)

print('---------------------------------------------')
result = ''
for x in s[::-1]:
    result += x
print(result)
print('-----------------------while----------------------')

for x in range(1, 11):
    print('Hello World')
print('-------------------------------------------')

num = int(input('Enter a positive number: \n'))
#num = int(num)

while num <= 0:
    num = int(input('Enter a positive number: \n'))
print(f'You have entered {num}')
print('---------------------------------------------')

answer = input('Enter yes or no:\n')

while not (answer.lower() == 'yes' or answer.lower() == 'no'):
    answer = input('Enter yes or no:\n')

print(f'You have entered  {answer}')




