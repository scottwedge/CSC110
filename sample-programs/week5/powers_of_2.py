# power_of_2.py
#
# print a list of powers of 2
# also includes input validation

# CSC 110
# Fall 2011


top = int(input('Enter a value between 1 and  20: '))

# an  indefinite loop for input validation
while top < 1 or top > 20:
    print('Error.  ' + str(top) + ' is not between 1 and 20. Please try again.')
    top = int(input('Enter a value between 1 and 20 '))

# a count controlled loop
for exp in range(0, top + 1):
    value = 2**exp
    print('2**' + str(exp) + ' = ' + str(value))
