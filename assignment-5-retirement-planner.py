# Assignment 5 - Retirement Planner - Part II
# CSC 110 - Section 03
# Justin Clark
# 1/27/2020

# import assignment-4 so we can use its calc_months function later
import importlib  
retirement_simulation = importlib.import_module('assignment-04-retirement-planner')

def displayWelcomeMessage():
    # display welcome message
    print('\nWelcome to the retirement planning tool!\n')

def createHeader():
    # create header for program output
    header = 'Retirement Savings Table:\n\n' + \
        'Starting   |\tAssumed Interest Rate\n' + \
        'Balance    |\t3% \t5% \t7% \t9% \n' + \
        '-----------+' + ('-' * 32) # <-- adds 32 dashes to the end, very cool!

    # display the header
    print(header)

def rateFormula(rate):
    """this function converts an integer representation 
    into its actual decimal percent equivillant.
    """
    return rate / (100 * 12)

def createTable():

    # loop has a stop value of 900001 so that 900000 will be included in the range
    for starting_balance in range(450000, 900001, 50000):
        
        # initialize row
        row = '$' + str(starting_balance) + '    |'

        # loop has a stop value of 10 so 9 will be included in the range
        for rate in range(3, 10, 2):
            months = retirement_simulation.calc_months(
                starting_balance,
                rateFormula(rate),
                monthly_spending
                )

            # append calculated months per rate to the current row
            row += '\t' + str(months)

        # write the row to the console
        print(row)

displayWelcomeMessage()

# get monthly spending amount from user
monthly_spending = float(input('Enter monthly spending (at least $500): $'))
while monthly_spending < 500:
    monthly_spending = float(input('TRY AGAIN -- monthly spending amount must be at least $500: '))

createHeader()
createTable()