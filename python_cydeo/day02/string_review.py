n = 'Automation Testing'

print(n[0])  # A
print(n[-1]) # g
print(len(n)) # 18
print(n[len(n) - 1]) # g


n = n.lower()
print(n) # automation testing

print('------------------------------------------------------------')

s = 'Python Programming Language'
language = s[0:6]
print(language) # Python

s2 = s[:18]
print(s2) # Python Programming
reversed_str = s[::-1]
print(reversed_str) # egaugnal gnimmargorP nohtyP


s = 'Python Programming Language'
reversed_str = ''.join(reversed(s))
print(reversed_str) # egaugnal gnimmargorP nohtyP

print('------------------------------------------------------------')

expected_title = 'Cydeo is the best'
actual_title = 'Cydeo is the besT'

print(expected_title.lower() == actual_title.lower()) # True


