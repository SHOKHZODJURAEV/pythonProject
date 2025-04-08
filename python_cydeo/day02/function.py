def return_value():
    return 1000

print(return_value()) # 1000

def return_integer() -> int:
    print('This is int function')

print(return_integer()) # None

def cube(num: int) -> int:
    return num * num * num

print(cube(3)) # 27

def addition(num1: int, num2: float, num3: int = 0) -> float:
    return num1 + num2 + num3

print(addition(5, 10)) # 15
print(addition(5, 10, 15)) # 30




