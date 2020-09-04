# Assignment 4 - Retirement Planner - Part I
# CSC 110 - Section 03
# Justin Clark
# 1/26/2020

# https://canvas.northseattle.edu/courses/1871665/assignments/16999840?module_item_id=38896156

# DUE 2/20 (THURSDAY)

def ordinal_number(num):
    """create string with ordinal representation of 
    number given
    """

    # 10 through 20 all get 'th' suffix
    if num >=10 and num <=20:
        suffix = 'th'
    # suffix for all other numbers depends on the last digit in the number
    else:
        last_digit = num % 10
        if last_digit == 1: suffix = 'st'
        elif last_digit == 2: suffix = 'nd'
        elif last_digit == 3: suffix = 'rd'
        else: suffix = 'th'
    return(str(num) + suffix)

def calc_rate(rate):
    """this function converts an integer representation 
    into its actual decimal percent equivillant
    """
    return rate / (100 * 12)

def calc_months(starting_balance, 
    
    rate, 
    
    monthly_withdrawl):
    """this function simulates a retirement account's 
    spending pattern and applied intrest earned until 
    the savings acccount is depleted or the simulated
    client reaches the maximum time in retirement
    """

    # reassign integer rate as calculated rate percentage
    rate = calc_rate(rate)

    # initialize variables
    balance = starting_balance
    months = 0
    total_withdrawls = 0

    # 600 months = 50 years, for the simplicity of this program, 
    #   we're assuming no one would live that long
    while balance > 0 and months < 600:
        balance -= monthly_withdrawl
        balance = balance + (balance * rate)
        total_withdrawls += monthly_withdrawl
        months += 1
        
        if balance <= 0:
            break

    # not to exceed 600 months per product requirements 
    else:
        return 600

    return months

if __name__ == "__main__":
    """this block of code will only be executed if this script
    is passed directly as a command to the Python interpreter.

    i.e., this code will not be executed when imported into assignment 5
    """

    # mock inputs/test cases::
    tests = [
        calc_months( 300000, 6, 3000 ),
        calc_months( 10000, 0, 2000 ),
        calc_months( 1000000, 4.5, 4200 ),
        calc_months( 1000000, 4.6, 4200 ),
        calc_months( 2000000, 5, 9050 )
    ]

    # create report header
    print(
        '-'*60 +
        ' '*20 + 'RETIREMENT SPENDING SIMULATION\n' +
        '-'*60 
    )

    # display how many months the savings lasted for each test case
    for test in tests:
        test_case = ordinal_number( tests.index(test) + 1)
        test_result = str(test)

        print(test_case +' test resulted in a total of: '+ test_result +' months of spending')

# =======================================================================
# Results of Test Cases (running program will give the following results)
# -----------------------------------------------------------------------
# 1st test resulted in a total of: 138 months of spending
# 2nd test resulted in a total of: 5 months of spending
# 3rd test resulted in a total of: 589 months of spending
# 4th test resulted in a total of: 600 months of spending
# 5th test resulted in a total of: 599 months of spending
# -----------------------------------------------------------------------
# All tests results match Excel spreadsheet used as benchmark 
# =======================================================================