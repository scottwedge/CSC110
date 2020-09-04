# Assignment 5 - Retirement Planner - Part II
# CSC 110 - Section 03
# Justin Clark
# 1/27/2020

# https://canvas.northseattle.edu/courses/1871665/assignments/16999842?module_item_id=38896157

# DUE: 2/25 (Tuesday)

# =======================================================================================
# This was the code I was using to import assignment 4
# ----------------------------------------------------
# # import assignment-4 so we can use its calc_months function later
# import importlib  
# retirement_simulation = importlib.import_module('assignment-4-retirement-planner')
# # USAGE::
# months = retirement_simulation.calc_months()

# =======================================================================================
def calc_months(starting_balance, rate, monthly_withdrawl):
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

# =======================================================================================

def displayWelcomeMessage():
    """display welcome message
    """
    print('\nWelcome to the retirement planning tool!\n')

def createHeader():
    """create header for program output
    """
    header = 'Retirement Savings Table:\n\n' + \
        'Starting   |\tAssumed Interest Rate\n' + \
        'Balance    |\t3% \t5% \t7% \t9% \n' + \
        '-----------+' + ('-' * 32) # <-- adds 32 dashes to the end, very cool!

    # display the header
    print(header)

def calc_rate(rate):
    """this function converts an integer representation 
    into its actual decimal percent equivillant.
    """
    return rate / (100 * 12)

def createTable():
    """creates retirement planning table
    """

    # loop has a stop value of 900001 so that 900000 will be included in the range
    for starting_balance in range(450000, 900001, 50000):
        
        # initialize row
        row = '$' + str(starting_balance) + '    |'

        # loop has a stop value of 10 so 9 will be included in the range
        for rate in range(3, 10, 2): 
            months = calc_months(
                starting_balance,
                rate,
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

# =======================================================================================
# this test case matches assignment example exactly when entering 5000
# --------------------------------------------------


# Welcome to the retirement planning tool!

# Enter monthly spending (at least $500): $5000
# Retirement Savings Table:

# Starting   |    Assumed Interest Rate
# Balance    |    3%      5%      7%      9%
# -----------+--------------------------------
# $450000    |    102     113     127     149
# $500000    |    115     129     150     183
# $550000    |    129     147     175     229
# $600000    |    143     166     205     300
# $650000    |    157     187     242     460
# $700000    |    172     210     288     600
# $750000    |    188     235     351     600
# $800000    |    204     263     453     600
# $850000    |    221     294     600     600
# $900000    |    239     331     600     600

# =======================================================================================
# this test case demonstrates an exaggerated spending 
# amount which require a higher rate of return.
# entering 6777, we see it would last 599 months at 9%
# --------------------------------------------------


# Welcome to the retirement planning tool!

# Enter monthly spending (at least $500): $6777
# Retirement Savings Table:

# Starting   |    Assumed Interest Rate
# Balance    |    3%      5%      7%      9%
# -----------+--------------------------------
# $450000    |    73      78      84      92
# $500000    |    82      88      97      107
# $550000    |    91      99      110     125
# $600000    |    100     111     124     145
# $650000    |    110     123     140     168
# $700000    |    120     135     158     197
# $750000    |    130     148     177     233
# $800000    |    140     162     199     283
# $850000    |    151     177     224     364
# $900000    |    162     193     253     599

# =======================================================================================
# this test case demonstrates a very conservative speeding 
# amount coupled with a very conservative rate of returns.
# entering 2893, we see it would last 599 months at 3%
# --------------------------------------------------


# Welcome to the retirement planning tool!

# Enter monthly spending (at least $500): $2893
# Retirement Savings Table:

# Starting   |    Assumed Interest Rate
# Balance    |    3%      5%      7%      9%
# -----------+--------------------------------
# $450000    |    197     250     400     600
# $500000    |    226     304     600     600
# $550000    |    258     375     600     600
# $600000    |    292     474     600     600
# $650000    |    330     600     600     600
# $700000    |    371     600     600     600
# $750000    |    417     600     600     600
# $800000    |    469     600     600     600
# $850000    |    529     600     600     600
# $900000    |    599     600     600     600
# =======================================================================================
