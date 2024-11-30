employee1:dict = {}


employee2:dict = {}
employee1['Name'] = 'John'
employee1['Age'] = 25
employee1['Gender'] = 'Male'
employee1['Salary'] = 50000

print(employee1)

employee2 = {
    'Name': 'James',
    'Age': 25,
    'Gender': 'Male',
    'Salary': 50000,
    'full_time': False
}

print(employee2)
print(employee1['Name'])
print(employee2['Name'])

employee2['Salary'] += 10000
print(employee2)
employee2.update({'Age': 35})
print(employee2)


employee2['full_time'] = True
employee2.update({'Gender': 'Female'})
print(employee2)
employee2.pop('Age')
print(employee2)
employee2.popitem()
print(employee2)



print('---------Iterating Dictionary-------------')

employee3 = {
    'Name': 'Sam',
    'Age': 27,
    'Gender': 'Male',
    'Salary': 140000,
    'job_title': 'Software Engineer',
    'full_time': False
}
print(list(employee3.keys()))

for key in employee3.keys():
    print(key)

test = employee2.copy()

print(test)

for key in employee2.keys():
    print(f'Key {key} has value {employee2[key]}')
print('----------------------------------------------------------------------')
result = list(employee3.values())
print(result)
print(type(result))

for value in employee3.values():
    print(value)

print('---------------------------------------------------')

for x in employee3.items():
    print(x)

print('-------------------------------------------------')

for x in employee3.items():   # items() returns a collection of tuples, in each tuple there will be two elements
    print(f'Key {x[0]} has value {x[1]}')
print('----------------------------------------------------------')

students = {
    'A01': {'Name': 'John', 'Age': 25, 'Gender': 'Male'},
    'A02': {'Name': 'Sam', 'Age': 26, 'Gender': 'Male'},
    'A03': {'Name': 'Kat', 'Age': 23, 'Gender': 'Female', 'Salary': [50000, 60000, 70000]},
}
print(students)
print(students['A03'])
print(students['A03']['Gender'])
students['A03']['Age'] = 24
print(students)
print('------------------------------------------------')

students['A01'].update({'Age': 30})

print(students)

students['A01']['Gender'] = 'Male'

print('-------------------------------------------------')

students['A03']['Salary'][1] = 10000000
print(students['A03'])
print('----------------------------------------------------')

for x in students['A03'].items():
    print(x)

print('---------------------------------------------------')

for x in students.items():
    print(x[1])
    for y in x[1]:
        print(y)

print('-----------------------------------------------------')

for value in students.values():
    print(value)
    for item in value.items():
        print(item)

print('----------------------------------------------------')







