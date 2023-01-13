
# Mapping Operator to function

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

    def __add__(self, other):
        return self.salary+ other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f'Employee("Name",Salary,"Role")'

    def __str__(self):
        return f'Employee("Name",Salary(int),"Role")'


sudarshan = Employee('Sudarshan', 1200000, 'Data Scientist')
any=Employee('Any',500000,'Intern')
navi=Employee('Naveen',1200000,'Programer')

print(sudarshan+navi)
print(sudarshan/any)
print(sudarshan)