
# sale_price.py

# This program gets an item's original price and
# calculates its sale price, with a 20% discount.

# Illustrates a named constant
# Illustrates an escape character (see p. 67)
# Illustrates format string and how to display the % character

# CSC 110
# 9/25/2011, updated 10/4/2016

DISCOUNT_RATE = 0.2   

print('This program will ask you for an item\'s price, ' \
      + 'then display the sale price.\n')

# Get the item's original price.
original_price = float(input('Enter the item\'s original price: '))

# Calculate the amount of the discount.
discount = original_price * DISCOUNT_RATE

# Calculate the sale price.
sale_price = original_price - discount

# Display the sale price.
print('Your product\'s original price is $' + format(original_price, '.2f'))
print('With a ' + format(DISCOUNT_RATE, '.1%') + ' discount of $' \
      + format(discount, '.2f') + ', the sale price is $' \
      + format(sale_price, '.2f') + '.')

# Test case:
# Enter the item's original price: 200
# Your product's original price is $200.00
# With a 20.0% discount of $40.00, the sale price is $160.00