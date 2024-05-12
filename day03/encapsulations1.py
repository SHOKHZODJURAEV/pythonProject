class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.salary = 0
        self.set_name(name)
        self.set_age(age)

    def get_name(self) -> str:
        if self.__name is None or self.__name == '' or type(self.__name) != str:
            raise RuntimeError(f'Invalid name has been set: {self.__name}')
        return self.__name

    def set_name(self, name: str):
        if type(name) != str:
            raise RuntimeError(f'Invalid name has been set: {name}')
        if name == '':
            raise RuntimeError(f'Person name can not be empty')
        self.__name = name

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int):
        if age < 0 or age > 100:
            raise RuntimeError(f'Invalid age has been set: {age}')
        self.__age = age

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


person1 = Person('John', 23)
person1.set_name('Bekzod')
person1.salary = 100
print(person1.__dict__)
print(person1.get_name())
print(person1)


