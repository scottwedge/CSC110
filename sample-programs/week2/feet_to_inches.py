
# feet_to_inches.py

# Program to convert from feet to inches.
# Output in inches is rounded to one place after the decimal point.
# CSC 110
# 9/25/2011, updated 10/4/2016

print("This program will convert feet to inches")
print()
print()

# get feet from user
feet = float(input("Enter distance in feet: "))

# convert
inches = feet * 12

#
print(str(feet) + ' ft = ' + format(inches, '.1f') + ' inches')

# Test cases, produced by the program and confirmed by hand:
# 12.0 ft = 144.0 inches
# 12.6 ft = 151.2 inches