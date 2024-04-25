import numbers


class Employee:
# static variable
# is_human = True

    def __init__(self, name: str = 'Unknown', job_title: str = 'Janitor', salary: numbers = 0):
        # instance variable
        self.name = name
        self.job_title = job_title
        self.salary = salary

    def work(self):
        print(f'{self.name}')
        print(f'{self.job_title}')

    def __str__(self):
        return f'{self.name}, {self.job_title}'


    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'





employee1 = Employee()
print(employee1.name)
print(employee1.job_title)
print(employee1.salary)

employee2 = Employee('Shawn')
print(employee2.name)
print(employee2.job_title)
print(employee2.salary)
employee3 = Employee('Brain', 'Python', 100)
print(employee3.name)
print(employee3.job_title)
print(employee3.salary)

print('-----------------------------------------------------------')

print(employee2.__str__())
employee1.work()


