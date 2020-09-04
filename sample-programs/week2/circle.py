
# circle.py

# Program to calculate area and circumference of a circle.
# NOTE: we import the math module so we can use the built-in definition for pi.
# The output section demonstrates formatting numbers for output;
# notice how the format function performs appropriate rounding.
# CSC 110
# 9/25/2011, updated 10/4/2016

import math

print("This program will ask for the radius of a circle then calculate the area and circumference")
print()
print()

# get radius
radius = float(input('Please enter radius: '))

# do the math.  Notice the syntax for using pi
area = math.pi * radius ** 2
circumference = math.pi * radius * 2

# output results
print('Given a circle with radius =' + str(radius))
print('The area = ' + format(area, '.4f') + ' and the circumference = ' \
      + format(circumference, '.4f'))


# test cases, confirmed by hand
# radius of 10 produces an area = 314.1593 and circumference = 62.8319
# radius of 1 gives area = 3.1416 and circumference = 6.2832