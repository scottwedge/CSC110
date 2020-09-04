# evenOdd2.py
#
# Even/odd program v2.
# displays whether user input is even or odd and positive or negative

# CSC 110
# Fall 2011

def main():
    print('How odd is this?')

    # get a user number
    number = int(input('Please enter an integer: '))

    # determine the characteristics
    if number < 0:
        if number % 2 == 0:
            print(str(number) + ' is a negative, even value')
        else:
            print(str(number) + ' is a negative, odd value')
    elif number > 0:
        if number % 2 == 0:
            print(str(number) + ' is a positive, even value')
        else:
            print(str(number) + ' is a positive, odd value')
    else:
        print('you entered 0')

# Call the main function.
main()