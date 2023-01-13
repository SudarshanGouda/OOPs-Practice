class Employee:
    no_of_leaves=15
    #class variable
    pass

sudarshan=Employee()
shivaraj=Employee()

print(sudarshan.no_of_leaves)
print(shivaraj.no_of_leaves)

Employee.no_of_leaves=20

print(sudarshan.no_of_leaves)
print(shivaraj.no_of_leaves)

sudarshan.no_of_leaves=25
# Instance variable


print(sudarshan.no_of_leaves)
print(shivaraj.no_of_leaves)