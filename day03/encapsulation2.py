
class Person:
    def __init__(self, name: str = 'Jimmy', age: int = 2):
        self.__name = None
        self.__age = None
        self.person_name = name
        self.person_age = age

    @property
    def person_name(self):
        if self.__name is None or self.__name == '' or type(self.__name) != str:
            raise RuntimeError(f'Invalid name has been set: {self.__name}')
        return self.__name
    
    @person_name.setter
    def person_name(self, name):

        if type(name) != str:
            raise RuntimeError(f'Invalid name has been set: {name}')
        if name == '':
            raise RuntimeError(f'Invalid name has been set: {name}')

        self.__name = name


person1 = Person()


person1.person_name = 'Daniel'
print(person1.person_name)

