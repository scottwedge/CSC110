# CSC 110 - Lab Activity - Function Definitions
# Section 03
# Justin Clark
# 2/19/2020

# DUE: 11pm Tonight

# https://canvas.northseattle.edu/courses/1871665/assignments/16999863?module_item_id=38896091

import math  # import statement needed for math.pi, math.sin() and math.cos() 

def main():
    # The following statements demonstrate the use of
    # math.pi, math.sin() and math.cos().  Study them
    # so you can apply these tools for Part 2 below.
    print('pi =', math.pi)
    print('sin(0) =', math.sin(0))
    print('cos(0) =', math.cos(0))
    deg45 = math.pi/4
    print('sin(45 deg) =', math.sin(deg45))
    print('cos(45 deg) =', math.cos(deg45))

    # PART 1:
    # Change the following statements by adding FUNCTION CALLS to 
    # the area_trapezoid() function as needed.  Your goal is to become
    # comfortable writing calls to functions that RETURN a value.
    # The table of data you need for reference is in the LAB INSTRUCTIONS.

    # Part 1a: Replace the number 1 below with an appropriate function call:
    print('\nPart 1a: The area shown on the FIRST table row is ' \
          + format(area_trapezoid(4, 5, 8), '.2f'))   
    # Part 1b: Replace the numbers 2 and 3 with appropriate function calls;
    # NOTICE that the number 33.1 is equal to 40.5 - 7.4:
    answer = area_trapezoid(2, 7, 9) - area_trapezoid(3.2, 4.2, 2)
    print('\nPart 1b: If you did it correctly, this should be 33.1: ' \
          + format(answer, '.1f'))
    
    # PART 2:
    # UN-Comment the following two statements after you have written
    # the show_sin_cos_squared_table() function definition.  When you
    # run the program, this part should show tables of numbers that
    # look exactly like the ones in the instructions.
    
    show_sin_cos_squared_table(8)
    show_sin_cos_squared_table(20)
    
    # END of 'main' function definition.

# a trapezoid has a height and a top length and bottom length.
# The top and bottom lengths are typically referred to as base2 and base1
# See this website for a picture  http://math.com/tables/geometry/areas.htm
# DO NOT MAKE ANY CHANGES TO THIS FUNCTION DEFINITION
def area_trapezoid(base1, base2, height):
    area = height / 2.0 * (base1 + base2)
    return area

# ADD your function definition for show_sin_cos_squared_table() here.
# Don't forget to include an appropriate COMMENT BLOCK for the function.

# In mathematics, the sine is a trigonometric function of an angle. The sine of an acute angle is defined in 
# the context of a right triangle: for the specified angle, it is the ratio of the length of the side that is 
# opposite that angle to the length of the longest side of the triangle (the hypotenuse)
# Cosine (cos) function - Trigonometry. In a right triangle, the cosine of an angle is the length of the adjacent side (A) divided by the length of the hypotenuse (H). ... In any right triangle, the cosine of an angle is the length of the adjacent side (A) divided by the length of the hypotenuse (H).
def show_sin_cos_squared_table(interval):
    """
    This function creates a data table with sine and cosine data.
    
    The function takes a parameter "interval", a number, and uses the interval 
    to determine the amount to step up from the previous number. The function
    then determines the number's sine, cosine, and the sum of both the squared 
    sine, and the squared cosine.
    """
  
    # creates a dashed line
    line = '-'*44+'\n'

    minN = 0
    maxN = math.pi*2

    # determine step amount
    step = (maxN) / (interval)
    
    # determine the amount of rows to print
    rows = interval + 1

    # print header
    print(
        line + \
        '  n' + \
        '\t sin(n)' + \
        '\t cos(n)' + \
        '\t sin^2(n) + cos^2(n)'
    )

    # print table rows 
    for i in range(rows):
        n = minN + i * step  # calculate the value of 'n' for row 'i'

        # do calculations
        sinN = math.sin(n)
        cosN = math.cos(n)
        sin_plus_cos = (sinN ** 2) + (cosN ** 2)

        # print current row with formated calculations
        print(
            format(n, '6.4f'), 
            format(sinN, '7.3f'), 
            format(cosN, '7.3f'),
            format(sin_plus_cos, '21.17f')
        )

    # print footer
    print(line, '\n')

main()