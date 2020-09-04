# evenOdd.py
#
# Even/odd program displays whether user input is even or odd

# CSC 110
# Fall 2011

def main():
    print('How odd is this?')

    # get a user number
    number = int(input('Please enter an integer: '))

    # test for even
    if number % 2 == 0:
        print(format(number, 'd') + ' is even')
    else:
        print(format(number, 'd') + ' is odd')
    # An alternative to format(number, 'd') would be str(number)

# Call the main function.
main()   