
# decimal_places

# This program demonstrates how a value can be
# formatted, rounded to different numbers of
# decimal places, using the %f placeholder
# CSC 110
# 9/25/2011, updated 10/4/2016

my_value = 1.123456789

# Python 3 output formatting using the 'format' function:
print(format(my_value, '.0f'))  # Rounded to 0 decimal place
print(format(my_value, '.1f'))  # Rounded to 1 decimal place
print(format(my_value, '.2f'))  # Rounded to 2 decimal places
print(format(my_value, '.3f'))  # Rounded to 3 decimal places
print(format(my_value, '.4f'))  # Rounded to 4 decimal places
print(format(my_value, '.5f'))  # Rounded to 5 decimal places
print(format(my_value, '.6f'))  # Rounded to 6 decimal places
print()

# Here is the Python 2 way to accomplish the same thing:
print('%.2f' % my_value)  # Rounded to 2 decimal places

input("Please press enter to continue")
print()
print()

# Here are some examples where you can insert a value
# into a more interesting string
num = 2.724565
print('The other value = ' + str(num)) # notice this doesn't round at all
print('Here ' + format(num, '.4f') + ' is rounded to 4 decimal places.')