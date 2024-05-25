unique_elements_dict = {}
unique_elements_set = set()

print(type(unique_elements_dict))
print(type(unique_elements_set))


unique_elements_set.add(10)
unique_elements_set.add(10)
unique_elements_set.add(20)
unique_elements_set.add(30)
unique_elements_set.add(30)
print(unique_elements_set)

# print(unique_elements_set[1]) no index

unique_elements_set.remove(10)
print(unique_elements_set)
unique_elements_set.update((90,80,70,60,50,40)) # inside update method is tuple value
print(unique_elements_set)

print(unique_elements_set.pop())
print(unique_elements_set)

print(help(set.pop))

print('---------------------------------------------------')


s1 = {'Java', 'Python', 'Ruby', 'Cydeo'}
s2 = {'Ruby', 'Java', 'C++', 'Swift', 'C#'}

s5 = s1.difference(s2)
print(s5)

set3 = s1.intersection(s2)
print(s1.intersection(s2))

# removes the elements of the first set that exist in the second set
a1 = {'Book', 'Pen', 'Apple', 'Cherry', 'Coffe'}
a2 = {'Book', 'Apple', 'Banana', 'Gradle', 'Coffe'}
a1.difference_update(a2)
print(a1)

print('----------intersection update-------------------')


b1 = {'Cydeo', 'Python', 'Java', 'C#', 'Wooden Spoon', 'Ruby', 'Swift'}
b2 = {'Wooden Spoon', 'Python', 'Cydeo', "C#", 'Check'}

b1.intersection_update(b2)
print(b1)

# Compares two sets and returns a new set which contains all elements except the common once
d1 = {'Cydeo', 'Python', 'Java', 'C#', 'Wooden Spoon', 'Ruby', 'Swift'}
d2 = {'Wooden Spoon', 'Python', 'Cydeo', "C#", 'Check'}

d5 = d1.symmetric_difference(d2)
print(d5)



