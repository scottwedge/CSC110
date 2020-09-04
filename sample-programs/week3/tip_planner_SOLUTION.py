# tip_planner_SOLUTION.py

# One possible SOLUTION for the Week #3 practice exercise.
# CSC 110

# Main function as provided in the instructions, unchanged.
def main():
    show_message()
    bill_amount = float(input('Please enter the amount of the bill: $'))

    show_tip(bill_amount, 15)
    show_tip(bill_amount, 18)
    show_tip(bill_amount, 20)
    show_tip(bill_amount, 25)

# Displays a welcome message to the user.
def show_message ():
    print('Welcome to the updated tip calculator.')
    print('This program will show you several options for a tip amount.\n')

# Caluclates and displays the tip amount for the percentage specified.
#   bill: the total amount of the bill before the tip is added
#   tip_percentage: the percentage tip desired
def show_tip (bill, tip_percentage):
    tip = bill * tip_percentage / 100
    print ('\nA '+ str(tip_percentage) + '% tip on a $' + format(bill, '.2f') \
           + ' bill amounts to $' + format(tip, '.2f') + '.')

main() # start the program


# Part 1 answers:

# apple 3 6 12
# banana 4 5 13
# cherry 6 3 15
# date 5 3 13
# elderberry 5.0 3 13.0
# fig 6.0 2 14.0
# ate 5 7 3

# IMPORTANT: Remember that the goal is to be able to analyze a program
#            like the one shown in Part 1 ON PAPER.  If you typed in
#            the program and ran it to get the results, be sure that you
#            practice solving problems like this without the help of
#            the computer.
 