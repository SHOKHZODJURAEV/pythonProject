
try:
    num = 10 / 0
    print(num)
except:
    print('something went wrong')
else:
    print('nothing went wrong')
finally:
    print('finally')
print('Test Complete')

print('------------------------------------')

tupleCheck = (10, 20, 30, 40, 50)
try:
    print(tupleCheck[2000])
except:
    print('index number is not valid')
else:
    print('index number is valid')


try:
    raise FileNotFoundError('No such file')
except SyntaxError:
    print('syntax error')
except OSError:
    print('OS error')
finally:
    print('finally')
raise LookupError('No such file')


