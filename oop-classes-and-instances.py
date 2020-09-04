# Python
# Object Oriented Programming
# Classes and Instances

class Employee:
    
    # __init__ is Python's constructor method
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullName(self):
        return '{} {}'.format(self.first, self.last)
    
    def empInfo(self):
        return 'Employee: {} {} \n${} {}'.format(self.first, self.last, self.pay, self.email)

emp1 = Employee('Justin', 'Clark', 90000)

print(Employee.empInfo(emp1))