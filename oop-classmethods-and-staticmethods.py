# Python
# Object Oriented Programming
# Classes and Instances

# https://www.youtube.com/watch?v=rq8cL2XMM5M

class Employee:

    company = 'iBest.com'
    raiseAmount = 1.4

    countOfEmployees = 0

    # __init__ is Python's constructor method
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@' + Employee.company

        Employee.countOfEmployees += 1
    
    def fullName(self):
        return '{} {}'.format(self.first, self.last)
    
    def empInfo(self):
        return 'Employee: {} {} \n${} {}'.format(self.first, self.last, self.pay, self.email)
    
    def applyRaise(self):
        self.pay = int(self.pay * self.raiseAmount)

print('Total Employees: ' + str(Employee.countOfEmployees))

emp1 = Employee('Justin', 'Clark', 90000)
emp2 = Employee('Joey', 'Clark', 100000)
emp3 = Employee('Lily', 'Clark', 110000)

print(Employee.company + 'Payroll Report')

print(Employee.empInfo(emp1))

Employee.applyRaise(emp1)

print(Employee.empInfo(emp1))

print('Total Employees: ' + str(Employee.countOfEmployees))

print(Employee.__dict__)
print(emp2.__dict__)
