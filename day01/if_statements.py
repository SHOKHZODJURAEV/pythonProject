if True:
    print('Python Programming')

print('Java Programming')

score = 70

if score >= 60:
    pass
    print('Congrats! you passed the exam')
"""
if(true){
}
"""
s = 'Hello World'
if 'H' and 'W' in s:
    print(s, 'has', 'H and W')

print('------------------------------')

if score >= 60:
    print('passed')
else:
    print('failed')
print('-----------------------------------')
age = 20
#result = None
if age >= 21:
    result = 'Eligible'
else:
    result = 'Not Eligible'

print('----------------------------------------')

# Ternary:
age = 26
result = 'Eligible' if age >= 21 else 'Not Eligible'
print(result)

num = 100
result = None
if num > 0:
    result = 'positive'
elif num < 0:
    result = 'negative'
else:
    result = 'Zero'

print(result)

print('------------------------------------')

result2 = 'Positive' if num > 0 else 'Negative'
print(result2)

score = -30
if score >= 70:
    print('passed')
elif score <= 70:
    print('failed')

if score >= 0 or score <= 100:
    if score >= 60:
        print('passed')
    else:
        print('failed')
else:
    print('Invalid score')

print('---------------------------------------------')
score = 92
if 0 <= score <= 100:
    if score >= 90:
        print('A')
    elif score >= 70:
        print('B')
    elif score >= 60:
        print('D')
    else:
        print('F')
else:
    pass
