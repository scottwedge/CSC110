# commission.py
#
# Program to calculate sales commission, and to accumulate a total
# uses loops and functions
#
# CSC 110
# Fall 2011

def main():
    print('You will be asked to enter sales and commission rate for' \
          + ' each employee.')
    print('The program will display the commission amount for each' \
          + '\nand the total for the company.\n')

    repeat = 'y'
    companyTotal = 0  # INITIALIZE ACCUMULATOR

    # repeated get the data for an employee and keep a running total
    while repeat == 'y' or repeat == 'Y':
        companyTotal += processOneEmp()
        repeat = input('\nIs there another employee? Enter y for yes: ')

   # display
    print('\n\nThe company\'s total commissions = $' + format(companyTotal, '.2f'))

# This function gets the data for one employee, calculates commission, 
# and displays it.
# Returns the commission for the employee.
def processOneEmp():

    #input
    name = input('\nWhat is the employee\'s name? ')
    sale = float(input('Enter the sales for ' + name + ' $'))
    rate = float(input('Enter the commission percentage rate for ' + name + ': '))

    #calculation
    total = sale * rate/100.0   # convert from percent to decimal

    # output
    print(name + ' earned $' + format(total, '.2f') + ' in commissions.')

    return total

main()
