import numbers

"""
Java Methods
    public statis void main(){
    }
"""


def display_message():
    print("Hello World!")
    print("Hello Python Function!")


display_message()


# Generic
def value():
    return 'Test'


print(value())


def return_int() -> int:
    return 10


print(return_int())

print('--------------------------------------')




def divide(num1, num2):
    return num1 / num2


print(divide(10, 2))


def square(num: int):
    return num * num


print(square(5))


def add(num1: int, num2: int):
    return num1 + num2


print(add(1, 5))


def minus(num4: float, num5: float) -> float:
    return num4 - num5


print(minus(5, 2))


print('-------------------------------------------------')


def calculate(num1:numbers, num2: numbers, operator:str) -> numbers:

    if operator == '-':
        return num1 - num2
    elif operator == '+':
        return num1 + num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        print('Invalid operator')
        return 0


print(calculate(5, 2, '+'))
print(calculate(2.2, 4.5, '*'))

print('-------------------------------------------------------------')

# example of method overloading


def sum(num1: int, num2: int, num3: int = 0, num4: int = 0) -> int:
    return num1 + num2 + num3 + num4


print(sum(10, 20))


class test:
    def test(self):
        pass


print('----------------------------------------------------------')


def concat(a: str, b, c='', d='', e=''):
    return a + b + c + d + e


print(concat('a', 'b', 'c', 'd', 'e'))


print(concat('Cydeo', 'School', '1', '5', 'True'))


"""
1. Declaring
2. parameters 
3. restricting parameter data type
4. setting default value to parameter
5. restricting return type

Dynamic Typing 
"""