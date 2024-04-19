name = 'Python'
totalIndex = len(name)
print(totalIndex)
print(name[0])
print(name[len(name)-1])
print(name[-1])
print(name[-2])


s = 'Java Programming'
print(s[5:16])
print(s[:4])
print(s[::-1])

t = 'Python Programming'

print(s[5:])
print('-------------------------------------------')

name = 'shawn wang'
test = name.capitalize()
# first is upper case
print(test)
check = s.title()

print(check)
print('-------------------------------------------')

r = '    Test      '
r = r.rstrip()
print(r)
print('--------------------------------------------')
print(name.index('a'))
print(name.rindex('a'))

s = 'Java Java'
b = s.replace('Java', 'Python', 1)
print(b)
print('--------------------------------------------')

ss = 'C# C# Python'
check1 = ss.replace('C#', 'look')
print(check1)

s = 'Java Java java java Java Python Python'

count_java = s.count('Java')
print(count_java)
count_java_lower = s.lower().count('java')
print(count_java_lower)

y = 'java'
h = 'JAVA'
print(y == h.lower())
print(s[0].islower())
print(s[2].islower())



