# arithmetic: +, -, *, /, %
print(10 - 2)
print(5 + 5)

print(10 * 3)

print(10 / 3)  # always return float value

print(10 % 3)

print(int(100 / 2))  # casting from float to int

# shorthand assignment operators: =, +=, -=, *=, /=, %=

a = 100
a = 200
print(a)

a += 100
print(a)

a -= 50
print(a)

a /= 2
print(a)

# Logical operators: and, or, not
s = 'Hello World'

print('H' and 'W' in s)

print(True and True)
print(True and False)

s = 'Java Python C# C++'
print('Java' or 'Ruby' in s)
print('------------------')
age = 29
citizen_ship = "USA"
is_eligible = age >= 18 and citizen_ship == "USA"

print(is_eligible)
has_java = 'Java' in s
print(has_java)
print('Python' not in s)
print(not False)
print(not True)
print('-----------------------------------------------------------------')
s = 'Java'
s2 = 'Java'

print(s is s2)




