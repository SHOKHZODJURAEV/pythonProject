
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'

    def work(self):
        print(f'{self.name} is working')


class Employee(Person):
    def __init__(self, name: str, age: int, job_title: str, company_name: str = 'Unknown', salary: int = 0):
        super().__init__(name, age) # calling Parent class constructor
        self.job_title = job_title
        self.company_name = company_name
        self.salary = salary


class Developer(Employee):

    def work(self):
        print(f'{self.job_title} {self.name} is coding')


class Teacher(Employee):
    def work(self):
        print(f'{self.name} teacher is working')


employee1 = Employee('Shawn', 30, 'QA', 'NextEra', 75000)
employee2 = Developer('Jack', 26, 'Programmer')
teacher = Teacher('Annie', 30, 'Chinese')
print(employee1)
print(employee2)
print(employee1.work())
print(employee2.work())
print(teacher.work())



