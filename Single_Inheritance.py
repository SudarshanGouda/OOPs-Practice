class Employee:
    no_of_leaves = 8

    def __init__(self, Name, Salary, Role):
        self.name = Name
        self.salary = Salary
        self.role = Role

    def printdetails(self):
        return (f'Name is {self.name} Salary is {self.salary} and role is {self.role}')

    # Use of class method
    @classmethod
    def change_leaves(cls, Leaves):
        cls.no_of_leaves = Leaves

    @classmethod
    def from_str(cls, string):
        parameter = string.split('-')
        return cls(parameter[0], parameter[1], parameter[2])

    @staticmethod
    def printgood(str):
        return (f'{str} is good')


class Programmer(Employee):

    def __init__(self,Name, Salary, Role,Language):
        self.name = Name
        self.salary = Salary
        self.role = Role
        self.languages=Language

    def printprogrammerdetails(self):
        return (f'Programmer name is {self.name} Salary is {self.salary} and role is {self.role}. '
                f'Langauages he kmows are {self.languages}')

sudarshan = Employee('Sudarshan', 1200000, 'Data Scientist')
any=Employee.from_str('Any-500000-Intern')
print(sudarshan.printdetails())


shiv=Programmer('shiva',1100000,'programmer',['python','Java'])
sam=Programmer('sam',1100000,'programmer',['python','Java'])

print(shiv.printprogrammerdetails())
print(sam.printgood('He'))

# print(sudarshan.no_of_leaves)
# sudarshan.change_leaves(33)
# print(sudarshan.no_of_leaves)

# print(any.printdetails())
# print(sudarshan.printgood('He'))