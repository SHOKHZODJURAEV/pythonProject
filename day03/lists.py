groceries = ['apple', 'orange', 'banana']
groceries.append('mango')
groceries.extend(('mango', 'kiwi', 'Grapes'))
print(len(groceries))
print(groceries)
groceries[-2] = 'Cherry'
print(groceries)
groceries.pop()
print(groceries)
print('---------------------------------------------------')
number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
number_list[2:-2] = [300, 4000, 5, 60000]
print(number_list)
print('----------------------------------------------------------------')
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(characters)
list1=characters[2: len(characters)-3]
print(list1)
list2 = characters[:4]
print(list2)
characters[2:5] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(characters)
print('--------------------------------------------------------')
names = ['John', 'Doe', 'Jim', 'Sally']
for x in names : print(x)
print('--------------------------------------------------------')
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(nums)
for i in range(0, len(nums)):
    nums[i] = nums[i] / 2
print(nums[i])

print('------------------------------------------------------')
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in reversed(range(len(nums))):
    print(nums[i])

print('--------------------Test-----------------------------')

for x in nums[::-1]:
    print(x)
print('---------777777----------------------------------')
for x in reversed(nums):
    print(x)

print('---------------------------------------------------')

i = 0

while i < len(nums):
    print(nums[i])
    i += 1

print('-----------------------------------------------')

for i in range(1, 6):
    print(i)

print('--------------------------')

nums = [60,100,90,80,70,60,50]

# nums.sort() # ascending order
nums.sort(reverse=True)
print(nums)

print('-----------------------------')
list3 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list3.reverse()
print(list3)
list3 = list(reversed(list3))
print(list3)
tuple_elements = ('apple', 'orange', 'banana')
print(tuple_elements)
print('-------------------------------')
list_elements = list(tuple_elements)
list_elements[-2] = 'C++'
list_elements.append('SWIFT')
print(list_elements)
tuple_elements = tuple(tuple_elements)
print(tuple_elements)

print('----------------------------')

list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(list1 is list2)

tuple1 = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
tuple2 = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

print(tuple1 is tuple2)

print('----------------------------------------')

groceries = ['apple', 'orange', 'banana']
groceries.append('mango')
groceries.extend(('mango', 'kiwi', 'Grapes'))
print(groceries)
groceries.remove('mango')
print(groceries)
groceries.pop()
print('----------------------------------------')
groceries.insert(2, 'Apple')
print(groceries)
print(groceries.index('banana'))

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(nums.count(1))

print('---------------Comprehensions------------------')
nums = []
for x in range(51):
    nums.append(x)
    print(nums)

print('---------------------------------')

divisible_by_5 = []

for x in nums:
    if x % 5 == 0:
        divisible_by_5.append(x)

print(divisible_by_5)

print('---------------Comprehensions------------------')
divisible_by_5 = [x for x in nums if x % 5 == 0]
print(divisible_by_5)
tuple_divisible_by_5 = ([x for x in nums if x % 5 == 0])

print('----------------------------------')

even_nums = [ x for x in nums if x % 2 == 0]
odd_nums = [ x for x in nums if x % 2 == 1]


print('------------------------------------------')

names = ['John', 'Doe', 'Jim', 'Sally', 'Doe', 'Doe', 'doe', 'Jim']

noDoe = [x for x in names if x.lower() != 'doe']
print(noDoe)





