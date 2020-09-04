# sin_cos_starter2017.py
# Starter code for the trapezoid / sin_cos_squared lab exercise.

# CSC 110
# Winter, 2017

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
          + format(1, '.2f'))   
    # Part 1b: Replace the numbers 2 and 3 with appropriate function calls;
    # NOTICE that the number 33.1 is equal to 40.5 - 7.4:
    answer = 2 - 3
    print('\nPart 1b: If you did it correctly, this should be 33.1: ' \
          + format(answer, '.1f'))
    


    # PART 2:
    # UN-Comment the following two statements after you have written
    # the show_sin_cos_squared_table() function definition.  When you
    # run the program, this part should show tables of numbers that
    # look exactly like the ones in the instructions.
    
    #show_sin_cos_squared_table(8)
    #show_sin_cos_squared_table(20)
    
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



main()
