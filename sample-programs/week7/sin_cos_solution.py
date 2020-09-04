# sin_cos_solution2017.py
# One possible solution for the trapezoid / sin_cos_squared lab exercise.

# CSC 110
# Winter, 2017

import math  # import statement needed for math.pi, math.sin() and math.cos() 

def main():

    # Part 1a: 
    print('\nPart 1a: The area shown on the table row is ' \
          + format(area_trapezoid(4, 5, 8), '.2f'))   
    # Part 1b: 
    answer = area_trapezoid(2, 7, 9) - area_trapezoid(3.2, 4.2, 2)
    print('\nPart 1b: If you did it correctly, this should be 33.1: ' \
          + format(answer, '.1f'))

    # Part 2:
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


# displays ("prints") a table containing (intervals + 1) rows
# showing values for 'n' ranging from 0 to 2pi and sin(n), cos(n), and
# (sin^2(n) + cos^2(n)) for each value of 'n'.
def show_sin_cos_squared_table(intervals):
    first = 0.0
    last = math.pi * 2
    step = (last - first) / intervals
    print('\n\n  n      sin(n)  cos(n)  sin^2(n) + cos^2(n)')
    for i in range(intervals + 1):
        num = i * step
        ans = math.sin(num) ** 2 + math.cos(num) ** 2
        print(format(num, '.4f') + format(math.sin(num), '8.3f') \
              + format(math.cos(num), '8.3f') + format(ans, '22.17f'))




main()
