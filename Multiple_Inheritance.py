class Employee:
    no_of_leaves = 8

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


class Player:
    no_of_games = 4

    def __init__(self, Name, Games):
        self.name = Name
        self.games = Games

    def printgamedetails(self):
        return f'The name of the player is {self.name},Games he play {self.games}'


class CoolProgrammer(Employee, Player):
    # As Employee is defined first it take (init) constructor from it only
    def printprogrammerdetails(self):
        return f'Programmer name is {self.name} Salary is {self.salary} and role is {self.role}.'


# sudarshan = Employee('Sudarshan', 1200000, 'Data Scientist')
# any=Employee.from_str('Any-500000-Intern')
sudarshan = CoolProgrammer('Sudarshan', 1200000, 'Data Scientist')
any = CoolProgrammer.from_str('Any-500000-Intern')

print(sudarshan.printprogrammerdetails())
print(any.printprogrammerdetails())
