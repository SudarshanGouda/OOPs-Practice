class Employee:
    no_of_leaves = 8 ## PublicVariable
    _no_of_el=33 ## Protected Variable
    _no_of_sl=2 ##Private Variable


    def __init__(self, Name, Salary, Role):
        self.name = Name
        self.salary = Salary
        self.role = Role

    def printdetails(self):
        return f'Name is {self.name} Salary is {self.salary} and role is {self.role}'

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
        return f'{str} is good'