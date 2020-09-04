
# future_value.py

# This program calculates future value, based on present value,
# annual interest rate, and time horizon.
# This program also demonstrates using the format function
# to format numbers for display to the user.

# CSC 110
# 9/25/2011, updated 10/4/2016

print('\nFuture Value Calculator\n\n')

# Get the desired future value.
presentValue = float(input('Enter the  prinicpal: '))

# Get the annual interest rate.
rate = float(input('Enter the annual interest rate [as a decimal]: '))

# Get the number of years that the money will appreciate. [Notice 'int'!]
years = int(input('Enter the number of years the money will grow: '))

# Calculate the amount this will grow to
futureValue = presentValue * (1.0 + rate)**years

# Display the future value
# notice the syntax when using multiple format operations in one print statement
print('\nLet $' + format(presentValue, '.2f') + ' grow for ' + str(years) \
      + ' years at an annual rate of ' + format(rate, '.2f'))
print('and you will end up with a total of $' \
      + format(futureValue, '.2f') + '.\n')


# Test cases, confirmed by hand
# $100 invested at 0.05 annual rate for 2 years will grow to $110.25
# $500 invested at 0.035 annual ratefor 10 years will grow to $705.30