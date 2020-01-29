# Assignment 4 - Retirement Planner - Part I
# CSC 110 - Section 03
# Justin Clark
# 1/26/2020

def calc_months(starting_balance, rate, monthly_withdrawl):
    """this function simulates a retirement account's 
    spending pattern and applied intrest earned until 
    the savings acccount is depleted or the simulated
    client reaches the maximum time in retirement 
    """

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

    # mock inputs::
    annual_interest_rate = float(6 / (100*12))
    starting_balance = float(900000)
    monthly_withdrawl = float(6000)

    # display how many months the savings lasted
    months = calc_months(
        starting_balance, 
        annual_interest_rate, 
        monthly_withdrawl
        )
    print('\ntotal months ' + str(months))

# exit loop method b)
    # if balance <= 0:
    #     print('\nbalance = ${:,.2f}'.format(balance))
    #     print('\nYour savings is wiped out, and you are hopefully not alive enough to worry about it anymore.')
    #     # total_withdrawls += balance # corrects for any excess monthly_withdrawl (balance <= 0)
    #     total_interest = total_withdrawls - starting_balance
    #     print('\nTotal interest = ${:,.2f}'.format(total_interest))
    # else:
    #     print('\nYour savings is still growing, you should have enjoyed more of your money while you where alive')
    #     print('\nRemaining balance = ${:,.2f}'.format(balance))
    # print('\nTotal monthly withdrawls = ${:,.2f}'.format(total_withdrawls))
