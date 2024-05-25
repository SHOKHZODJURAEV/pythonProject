from typing import final

pi: final = 3.14


pi = 3.5

print(pi)


@final
class Animal:
    pass


class Dog(Animal):
    pass


class Employee:

    @final
    def work(self):
        print("I am an Employee.")


class Driver(Employee):

    @final
    def _final_work(self):
        print("I am a Driver.")


class Person:

    def __init__(self, age: int):
        self.__age = age

    @property
    def person_age(self):
        return self.__age

    @person_age.setter
    def person_age(self, age: int):
        raise RuntimeError(f'Person age cannot be changed.')


PersonTest = Person(20)

PersonTest.person_age = 25

print(PersonTest.person_age)

