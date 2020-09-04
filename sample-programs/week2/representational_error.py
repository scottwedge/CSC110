
# representational_error.py
# 
# A demonstration of representational error
# CSC 110
# Sp'12


message = """The sequence of Python statements in this file demonstrates that even very
simple calculations, such as repeatedly adding 0.1 to a number, can result
in very small errors in the result.  This kind of error is normal and is
related to the way in which 'floating point' numbers are represented
(stored) in the computer.  All numbers are stored in a binary (base 2)
format, and conversions from a binary to a decimal (base 10) format are
not perfect, in the same way that it is difficult to represent the number
1/3 in a decimal format.  When viewing the output produced by the first
section of this program, you will notice that the decimal value shown is
sometimes a tiny bit larger or smaller than it should be. 

These errors are rarely of any consequence in normal calculations.
However, they do make it impossible to reliably test whether or not a
floating point number is exactly equal to some value.  Rather, we usually
test to see if two floating point numbers are equal to within some small
allowable error.\n"""

print(message)

x = 0.1
print(x)
x += 0.1  # UPDATE the value of x
print(x)
x += 0.1
print(x)
x += 0.1
print(x)
x += 0.1
print(x)
x += 0.1
print(x)
x += 0.1
print(x)
x += 0.1
print(x)
x += 0.1
print(x)

print()

message = """The same sequence of numbers as above is repeated below, but the 'format'
function is used to display each number with a fixed number of digits after
the decimal point.  

When the 'format' function is called as it is in this program, the function
returns a STRING representation of the numeric value with the specified
number of digits after the decimal point, even if one or more of the 
trailing digits are zeros.  The function also automatically rounds the
number in an appropriate way.

Because 'format' returns a STRING value, it should be used only to display
a numeric result to the user in a visually pleasing way.  Use the 'round'
function to round numbers that must be used in further calculations.  The
'round' function returns a numeric value (type int).\n"""

print(message)

x = 0.1
print(format(x, '.1f'))
x += 0.1
print(format(x, '.2f'))
x += 0.1
print(format(x, '.3f'))
x += 0.1
print(format(x, '.4f'))
x += 0.1
print(format(x, '.3f'))
x += 0.1
print(format(x, '.3f'))
x += 0.1
print(format(x, '.3f'))
x += 0.1
print(format(x, '.3f'))
x += 0.1
print(format(x, '.3f'))

print()

x = 11223344.5566
print(format(x, '.2f'))
print(format(x, ',.2f'))

