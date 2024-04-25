
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", 1, 2, 3, 4, 5, 6, 7, 8, 9, True, False)

print(type(days))
print(len(days))
print(days)

# get access index value
print(days[0])
print(days[-1])

work_day = days[0:5]

print(work_day)

week_days = days[:-13]
print(week_days)

weekend = days[-13:]
print(weekend)

tuple1 = (1,2,3)
tuple2 = (1,2,3)

print(tuple1 == tuple2)
print(tuple1 is tuple2) # in the same object checking memory address

tuple3 = tuple1 + tuple2
print(tuple3)

tuple4 = tuple1 * 5
print(tuple4)

reversed_tuple1 = days[::-1]
print(reversed_tuple1)

reversed_tuple2 = tuple(reversed(days))
print(reversed_tuple2)

print(days.index('Friday'))

numbers = (10, 10, 10, 10, 10, 20, 20, 30, 30, 40, 50, 10, 60, 10, 70)
print(numbers.count(10))

print('-------------------------------------------------------------')

for x in days:
    print(x)

print('--------------------------------------')

for x in range(0, len(days)):
    print(x)

print('-------------------------------------------')
for x in reversed(range(0, len(days))):
    print(x)
