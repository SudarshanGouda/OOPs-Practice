class Employee:

    no_of_leaves=8
    def __init__(self, Name, Salary, Role):
        self.name = Name
        self.salary = Salary
        self.role= Role

    def printdetails(self):
        return (f'Name is {self.name} Salary is {self.salary} and role is {self.role}')

    # Use of class method
    @classmethod
    def change_leaves(cls,Leaves):
        cls.no_of_leaves=Leaves

sudarshan = Employee('Sudarshan', 1200000, 'Data Scientist')
any=Employee('Any',500000,'Intern')
navi=Employee('Naveen',1200000,'Programer')


print(type(sudarshan))

print(dir(sudarshan))

print(id(sudarshan))

import inspect

print(inspect.getmembers(sudarshan))