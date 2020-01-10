# CSC 110 - Self Assignment #1
# Change a number of any base (except hexadecimal) to base 10
# Section 03
# Justin Clark
# 1/8/2020

# Create localized scope for program variables
def initializeProgram():

    numberToConvert = int(input('Please enter a number you wish to convert to Base 10: '))

    # We want to avoid hard coding numeric values that might need to change
    originalBase = int(input('Please enter the starting Base, then I\'ll convert it to Base 10: '))
    desiredBase = 10 # Keeping variable generic, may combine other binary functions into one program

    # Main function
    def convertToBase10(originalBase, numberToConvert):

        # Create array of digits from the number inputted
        arrayOfDigits = list(str(numberToConvert))

        # Need to work with the reversed array for index values to align with proper exponent positions
        reversedArrayOfDigits = arrayOfDigits[::-1]

        # Integer variable to hold the sum (answer)
        sumTotal = 0

        # For each digit (element) in the array:
        #   Raise original base to the power of the index value
        #   Then multiply by that digit, and add answer to the sum
        for (index, element) in enumerate(reversedArrayOfDigits):
            element = int(element)
            
            if originalBase == 2:
                # Only allow 1's and 0's if converting from base 2
                if element < 0 or element > 1:
                    return 'invalid input'
                else:
                    sumTotal = sumTotal + (element * (originalBase ** index))
            else:
                sumTotal = sumTotal + (element * (originalBase ** index))
        return sumTotal

    # Create subscript for displaying each base
    subscript = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    baseConvertedFrom = str(originalBase).translate(subscript)
    baseConvertedTo = str(desiredBase).translate(subscript)

    # Display the answer to the user
    convertedAnswer = convertToBase10(originalBase, numberToConvert)
    formatedAnswer = str(numberToConvert) + baseConvertedFrom + ' has been converted to ' + str(convertedAnswer) + baseConvertedTo
    print(formatedAnswer)


# Run the program
initializeProgram()
