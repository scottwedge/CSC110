# rectangle.py
#
# Demonstrates a programmer-defined function with parameters.
# Demonstrates the use of a FUNCTION comment block (not the
# same thing as this program-level comment block).
# Every function should have a comment block right before the
# line that begins with 'def' saying 1) what the function does
# and 2) how its parameters are used, including any restrictions
# on parameter values or data types.
#
# CSC 110
# 1/2020


# named constants
DEFAULT_WIDTH = 12.34
DEFAULT_HEIGHT = 34.56


# Shows the perimeter and area of the specified rectangle.
# The parameter width and height are the dimensions of the
# rectangle and must be numbers (type int or float).
def show_rectangle_info(width, height):
    # processing
    perimeter = 2 * (width + height)
    area = width * height

    # output
    print('\nA rectangle with a width of ' + format(width, '.2f') \
          + ' and a height of ' + format(height, '.2f') \
          + ' \nhas a perimeter of ' + format(perimeter, '.2f') \
          + ' and an area of ' + format(area, '.2f') + '.')
    
    
def main():
    # input (get some info from the user; save NUMBERS in the variables)
    width = float(input('What is the width of the rectangle? '))
    height = float(input('What is the height of the rectangle? '))
    
    # output (some sample function calls)
    show_rectangle_info(width, height)
    show_rectangle_info(25, 32)
    show_rectangle_info(DEFAULT_WIDTH, DEFAULT_HEIGHT)
    
main()    
