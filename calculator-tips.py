# CSC 110 - Practice Activity #2
# Tip Calculator
# Section 03
# Justin Clark
# 1/14/2020

# input
billAmountEntered = float(input('Enter bill amount $: '))
tipPercentEntered = float(input('Enter tip %: '))

# processing
tipCalculated = billAmountEntered * (tipPercentEntered / 100)
amountToPay = billAmountEntered + tipCalculated

# output (build receipt):
receipt = \
    '--------------------------' + '\n' + \
    'Receipt\n' \
    '-------------------' + '\n' + \
    'Bill Entered: ${:.2f}'.format(billAmountEntered) + '\n' + \
    'Tip Entered: {}%'.format(tipPercentEntered) + '\n' + \
    '-------------------' + '\n' + \
    'Tip Calculated: ${:.2f}'.format(tipCalculated) + '\n' + \
    'Amount Owed: ${:.2f}'.format(amountToPay) + '\n' + \
    '--------------------------'

print(receipt)