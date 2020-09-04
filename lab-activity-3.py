# CSC 110 - Lab Activity #3
# Simple Functions with Parameters
# Section 03
# Justin Clark
# 1/22/2020


# Part 1:
# ==============
#     print(s, a, b, c)
#   output: apple 3 6 12
#   output: banana 4 5 13
#   output: cherry 6 3 15
#   output: date 5 3 13
#   output: elderberry 5 3 13
#   output: fig 6 2 14
#   output: ate 6 3 15


# Part 2:
# ==============

def show_message():

    message = "\nWelcome to the updated tip calculator.\n" \
        + "This program will show you several options for a tip amount.\n"

    print(message)

def show_tip(billAmount, tipPercent):

    tipCalculated = billAmount * (tipPercent / 100)

    tipMessage = "A {}% tip on a ${:.2f} bill amounts to ${:.2f}." \
        "\n".format(tipPercent, billAmount, tipCalculated)
    
    print(tipMessage)

def main():

    show_message()

    bill_amount = float(input('Please enter the amount of the bill: $'))
    print('\n')

    show_tip(bill_amount, 15)
    show_tip(bill_amount, 18)
    show_tip(bill_amount, 20)
    show_tip(bill_amount, 25)

main() # start the program
