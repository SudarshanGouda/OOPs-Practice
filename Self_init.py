# class Employee:
#     no_of_leaves=15
#     #class variable
#
#     ## Methods
#     def printdetails(self):
#         return (f'Name is {self.name} Salary is {self.salary} and role is {self.role}')
#     ## self means on which object function is operated
#
# sudarshan=Employee()
# sudarshan.name='Sudarshan'
# sudarshan.salary=1200000
# sudarshan.role='Data Scientist'
#
# print(sudarshan.printdetails())
# ## sudarshan stands for self here


class Employee:

    def __init__(self, Name, Salary, Role):
        self.name = Name
        self.salary = Salary
        self.role= Role

    def printdetails(self):
        return (f'Name is {self.name} Salary is {self.salary} and role is {self.role}')


sudarshan=Employee('Sudarshan',1200000,'Data Scientist')

print(sudarshan.printdetails())
