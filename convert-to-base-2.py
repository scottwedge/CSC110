# CSC 110 - Self Assignment #2
# Change a number to base 2
# Section 03
# Justin Clark
# 1/9/2020

# Create localized scope for program variables
def initializeProgram():

    numberToConvert = int(input('Please enter a number you wish to convert to Base 2: '))

    # We want to avoid hard coding numeric values that might need to change
    originalBase = 10 # Assuming base 10
    desiredBase = 2 # Keeping variable generic, may combine other binary functions into one program

    # Initialize division variables
    dividend = numberToConvert
    divisor = desiredBase
    quotient = int(dividend / divisor)
    remainder = dividend % divisor

    # Answer variable
    stringBinary = ''

    # Main function
    def convertToBase2(dividend, divisor, quotient, remainder, stringBinary):

        # Divide the "desired" base into the number to convert, save the remainder 
        quotient = int(dividend / divisor)
        remainder = dividend % divisor

        # Reassign the last quotient as the new dividend
        dividend = quotient

        # Append new remaiders to string
        stringBinary += str(remainder)

        # Recursively run this function to divide until quotient is zero
        if quotient == 0:
            # The binary string is created backwards, so we need to reverse it
            reverseStringBinary = stringBinary[::-1]
            # Return the answer
            return reverseStringBinary 
        else:
            # Recursion point, feed current variables back in as the new values
            return convertToBase2(dividend, divisor, quotient, remainder, stringBinary)

    # Create subscript for displaying each base
    subscript = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    baseConvertedFrom = str(originalBase).translate(subscript)
    baseConvertedTo = str(desiredBase).translate(subscript)

    # Display the answer to the user
    convertedAnswer = convertToBase2(dividend, divisor, quotient, remainder, stringBinary)
    formatedAnswer = str(numberToConvert) + baseConvertedFrom + ' has been converted to ' + str(convertedAnswer) + baseConvertedTo
    print(formatedAnswer)
    
# Run the program
initializeProgram()
